from time import sleep
from celery import shared_task


@shared_task()
def task_1():
    sleep(5)
    return None


@shared_task()
def task_2():
    sleep(5)
    return None


@shared_task()
def task_3():
    sleep(5)
    return None


@shared_task()
def task_4():
    sleep(5)
    return None
