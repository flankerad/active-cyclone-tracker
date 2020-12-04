from __future__ import absolute_import
import logging
from celery import Celery
from celery.schedules import crontab
from config import CELERY_BROKER_URL, CYCLONE_URL, TASK_INTERVAL
from app.crawler import get_active_cyclones
from app.db import insert_data, close_connection
from connection import create_connection
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

'''
Run task.
Fetch data from website
store data in postgres
run task periodically
'''

app = Celery('tasks',
            broker=CELERY_BROKER_URL,
            backend=CELERY_BROKER_URL)

app.conf.update(
    timezone='UTC',
)

app.conf.beat_schedule = {
    'add-every-1-hour': {
        'task': 'tasks.active_cyclones',
        'schedule': crontab(minute=TASK_INTERVAL)
    },
}

@app.task
def active_cyclones():
    conn = create_connection()

    logger.info("Running active cyclone tasks")
    now = datetime.now()

    logger.info(now.strftime("%H:%M:%S"))

    data = get_active_cyclones(CYCLONE_URL)
    insert_data(conn, data)

    close_connection(conn)