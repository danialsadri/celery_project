from celery import shared_task
from config.celery import app
from celery.schedules import crontab
from datetime import timedelta


# app.conf.beat_schedule = {
#     'task_1': {
#         'task': 'notifications.tasks.schedule_tasks.task_1',
#         'schedule': crontab(minute='*/1'),
#     },
#     'task_2': {
#         'task': 'notifications.tasks.schedule_tasks.task_2',
#         'schedule': timedelta(seconds=30),
#     },
# }


@shared_task()
def task_1():
    print('running task 1')


@shared_task()
def task_2():
    print('running task 2')
