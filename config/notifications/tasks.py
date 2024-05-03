from time import sleep
from celery import shared_task


@shared_task()
def task_1(queue='celery'):
    sleep(5)
    return None


@shared_task()
def task_2(queue='celery:1'):
    sleep(5)
    return None


@shared_task()
def task_3(queue='celery:2'):
    sleep(5)
    return None


@shared_task()
def task_4(queue='celery:3'):
    sleep(5)
    return None
