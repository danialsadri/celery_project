import logging
from celery import shared_task, group


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


@shared_task(autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def raise_error_3():
    raise ConnectionError('connection error........................')


phone_numbers = [
    '09021234567',
    '09125469807',
    '09220986534',
    '09036578756',
]


@shared_task()
def send_sms_to_user(phone_number):
    if phone_number.startswith('0903'):
        raise ValueError(f'invalid phone number {phone_number}')
    else:
        return f'message has been sent to {phone_number}'


def handle_result(result):
    if result.successful():
        print(f'Task complete: {result.get()}')
    elif result.failed() and isinstance(result.result, ValueError):
        print(f'Task failed: {result.result}')
    elif result.status == 'REVOKED':
        print(f'Task was revoked: {result.id}')


def run_tasks():
    task_group = group(send_sms_to_user.s(phone_number) for phone_number in phone_numbers)
    result_group = task_group.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)
    for result in result_group:
        handle_result(result)
