from connection import pg_conn, redis_conn
from crawler import get_active_cyclones

pg_cur = pg_conn.cursor()
tableName = 'cyclone'


init_table = '''CREATE TABLE IF NOT EXISTS cyclone (
                cid varchar(45) NOT NULL,
                name varchar(45) NOT NULL,
                region varchar(45) NOT NULL,
                url varchar(450),
                img varchar(450),
                speed varchar(45),
                ctype  varchar(45),
                PRIMARY KEY (cid)
            ) '''

args = [cur.morgify(f'({cid}, {name}, {region}, url{}, {img}, {speed})', x) for x in data]
args_str =  ', '.join(args)



def insert_data(data):
    args = get_active_cyclones()
    insert_data = f'''
                BEGIN;
                TRUNCATE TABLE {tableName};
                INSERT INTO
                    cyclone (cid, name, region, url, img, speed)
                VALUES {args} ON CONFLICT DO NOTHING;
                COMMIT;
            '''
    pg_cur.execute(insert_data)






