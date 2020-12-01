from __future__ import absolute_import
import logging
from celery import Celery
from celery.schedules import crontab
from config import CELERY_BROKER_URL, CYCLONE_URL
from crawler import get_active_cyclones
from db import insert_data
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
        'schedule': crontab(minute='*/60')
    },
}

@app.task
def active_cyclones():
    print("Running Active Cyclone Task")
    logger.debug("Running active cyclone tasks")
    now = datetime.now()

    logger.debug(now.strftime("%H:%M:%S"))

    data = get_active_cyclones(CYCLONE_URL)
    insert_data(data)