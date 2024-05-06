import logging
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


@shared_task()
def send_message(mobile, message):
    sleep(5)
    return f'sms sent to user with {mobile} number and message was: {message}'


@shared_task()
def send_sms():
    sleep(5)
    return 'sms has been sent to user'


@shared_task()
def raise_error_1():
    try:
        print('this is my task')
        raise ValueError('value is not valid')
    except Exception:
        logging.error('an exception has been occurred')
        raise ConnectionError('connection error')
