from __future__ import absolute_import

import redis
import psycopg2
import config as config


pg_conn = psycopg2.connect(database=config.POSTGRES_DB,
                        user=config.POSTGRES_USER,
                        password=config.POSTGRES_PASSWORD,
                        host=config.POSTGRES_HOST,
                        port=config.POSTGRES_PORT)

redis_conn = redis.Redis(host=config.REDIS_HOST,
                port=config.REDIS_PORT)

