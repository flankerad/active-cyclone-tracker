import os


POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

BROKER_HOST = os.environ.get('REDIS_HOST')
BROKER_PORT = os.environ.get('REDIS_PORT')
BROKER_PASSWORD = os.environ.get("REDIS_PASSWORD")
BROKER_DB = 0

CYCLONE_URL = "https://rammb-data.cira.colostate.edu/tc_realtime/"

CELERY_BROKER_URL=f"redis://{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_DB}"
