from datetime import timedelta
from celery import shared_task
from config.celery import app

app.conf.beat_schedule = {
    'task_1': {
        'task': 'notifications.tasks.schedule_tasks.task_1',
        'schedule': timedelta(seconds=5),
    },
    'task_2': {
        'task': 'notifications.tasks.schedule_tasks.task_2',
        'schedule': timedelta(seconds=10),
    },
}


@shared_task()
def task_1():
    print('running task 1')


@shared_task()
def task_2():
    print('running task 2')
