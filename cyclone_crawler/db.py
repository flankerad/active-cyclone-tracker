from psycopg2 import errors
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


tableName = 'cyclones'


def insert_data(conn, args):
    query = f'''
                BEGIN;
                TRUNCATE TABLE cyclones;
                INSERT INTO
                    cyclones
                    (cid, name, speed, type, region, url, img, updated_at)
                    VALUES {args};
                COMMIT;
            '''
    pg_cur = conn.cursor()
    morg = pg_cur.mogrify(query)
    logger.info(morg)

    pg_cur.execute(query)


def close_connection(conn):
    return conn.close()


def get_data(conn, params):
    query = query_builder(params)
    pg_cur = conn.cursor()
    logger.info(pg_cur.mogrify(query))
    pg_cur.execute(query)
    data = pg_cur.fetchall()

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

    query = f'''SELECT {selector} FROM cyclones {where_clause};'''

    return query