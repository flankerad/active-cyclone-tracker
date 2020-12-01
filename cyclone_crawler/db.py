from connection import pg_conn
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

pg_cur = pg_conn.cursor()
tableName = 'cyclone'

def init_table():
    query = '''CREATE TABLE IF NOT EXISTS cyclone (
                    cid varchar(50) NOT NULL,
                    name varchar(50) NOT NULL,
                    region varchar(50) NOT NULL,
                    url varchar(150),
                    img varchar(255),
                    speed varchar(45),
                    type  varchar(45),
                    updated_at TIMESTAMP NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (cid)
                ) '''
    pg_cur.execute(query)

def insert_data(args):
    query = f'''
                BEGIN;
                TRUNCATE TABLE cyclone;
                INSERT INTO
                    cyclone
                    (cid, name, speed, type, region, url, img, updated_at)
                    VALUES {args} ON CONFLICT DO NOTHING;
                COMMIT;
            '''
    morg = pg_cur.mogrify(query)
    logger.debug(morg)

    pg_cur.execute(query)

def close_connection():
    return pg_conn.close()

def get_data(params):
    query = query_builder(params)
    pg_cur.execute(query)
    data = pg_cur.fetchall()
    close_connection()
    return data



def query_builder(params):
    selector = '*'
    where_clause = ''
    a = ' and '

    fields = params.get('fields')
    cond = params.get('conditions')

    if fields:
        selector = fields

    if cond and len(cond) > 1:
        for c in cond:
            where_clause = where_clause + f'where {c}{a}'
        where_clause = where_clause[:-5]

    elif cond:
        where_clause = f'where {cond[0]}'

    query = f'''SELECT {selector} FROM cyclone {where_clause};'''

    logger.info(pg_cur.mogrify(query))

    return query