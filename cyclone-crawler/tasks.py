from celery import Celery
from config import CELERY_BROKER_URL
from crawler import get_active_cyclones



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

# Save data in db
def save_data(args):
    #save data
    pass

@app.task
def fetch_data(x, y):
    #fetch data
    return x+y