import logging
from celery import shared_task


@shared_task()
def raise_error_1():
    try:
        print('this is my task')
        raise ValueError('value is not valid')
    except Exception:
        logging.error('an exception has been occurred')
        raise ConnectionError('connection error')


@shared_task()
def raise_error_2():
    raise ConnectionError('connection error')
