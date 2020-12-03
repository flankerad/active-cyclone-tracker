import os


HOST_NAME = os.environ.get('HOST_NAME', 'localhost')
HOST_PORT = os.environ.get('HOST_PORT', 8080)

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'flanker')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'cyclones')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)

BROKER_HOST = os.environ.get('REDIS_HOST', 'localhost')
BROKER_PORT = os.environ.get('REDIS_PORT', 6379)
BROKER_PASSWORD = os.environ.get("REDIS_PASSWORD", '')
BROKER_DB = 0
BACKEND_DB = 1

CYCLONE_URL = "https://rammb-data.cira.colostate.edu/tc_realtime/"

CELERY_BROKER_URL=f"redis://{BROKER_HOST}:{BROKER_PORT}/{BROKER_DB}"
CELERY_BACKEND_URL=f"redis://{BROKER_HOST}:{BROKER_PORT}/{BACKEND_DB}"

TASK_INTERVAL= os.environ.get('TASK_INTERVAL', '*/60')
KEYS = ('id', 'name', 'region', 'url', 'img', 'speed', 'type', 'updated_at', 'created_at')