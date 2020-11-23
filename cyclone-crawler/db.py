from connection import pg_conn, redis_conn

pg_cur = pg_conn.cursor()

init_table = '''CREATE TABLE IF NOT EXISTS cyclone (
                stormid varchar(45) NOT NULL,
                name varchar(45) NOT NULL,
                region varchar(45) NOT NULL,
                stormurl varchar(450) NOT NULL,
                PRIMARY KEY (stormid)
            ) '''

pg_cur.excute(init_table)