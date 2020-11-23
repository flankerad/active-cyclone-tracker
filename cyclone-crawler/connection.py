import redis
import psycopg2
from config import *


pg_conn = psycopg2.connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host=POSTGRES_HOST,
                        port=POSTGRES_PORT)


redis_conn = redis.Redis(host=REDIS_HOST,
                port=REDIS_PORT)


