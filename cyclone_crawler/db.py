from connection import pg_conn
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

pg_cur = pg_conn.cursor()
tableName = 'cyclone'


init_table = '''CREATE TABLE IF NOT EXISTS cyclone (
                cid varchar(50) NOT NULL,
                name varchar(50) NOT NULL,
                region varchar(50) NOT NULL,
                url varchar(150),
                img varchar(255),
                speed varchar(45),
                type  varchar(45),
                updated_at TIMESTAMP NOT NULL DEFAULT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (cid)
            ) '''


def insert_data(args):
    insert_data_args = f'''
                BEGIN;
                TRUNCATE TABLE cyclone;
                INSERT INTO
                    cyclone
                    (cid, name, speed, type, region, url, img)
                    VALUES {args} ON CONFLICT DO NOTHING;
                COMMIT;
            '''
    morg = pg_cur.mogrify(insert_data_args)
    logger.debug(morg)
    
    pg_cur.execute(insert_data_args)
