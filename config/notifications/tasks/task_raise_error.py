import logging
import sys
from celery.signals import task_failure
from celery import shared_task, group, chain
from time import sleep


# @shared_task()
# def raise_error_1():
#     try:
#         print('this is my task')
#         raise ValueError('value is not valid')
#     except Exception:
#         logging.error('an exception has been occurred')
#         raise ConnectionError('connection error')


# @shared_task()
# def raise_error_2():
#     raise ConnectionError('connection error')


# @shared_task(autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
# def raise_error_3():
#     raise ConnectionError('connection error........................')


# -------------------------------------------------------------------------------------------------------------------------------
# phone_numbers = [
#     '09021234567',
#     '09125469807',
#     '09220986534',
#     '09036578756',
# ]


# @shared_task()
# def send_sms_to_user(phone_number):
#     if phone_number.startswith('0903'):
#         raise ValueError(f'invalid phone number {phone_number}')
#     else:
#         return f'message has been sent to {phone_number}'


# def handle_result(result):
#     if result.successful():
#         print(f'Task complete: {result.get()}')
#     elif result.failed() and isinstance(result.result, ValueError):
#         print(f'Task failed: {result.result}')
#     elif result.status == 'REVOKED':
#         print(f'Task was revoked: {result.id}')


# def run_tasks_group():
#     task_group = group(send_sms_to_user.s(phone_number) for phone_number in phone_numbers)
#     result_group = task_group.apply_async()
#     result_group.get(disable_sync_subtasks=False, propagate=False)
#     for result in result_group:
#         handle_result(result)


# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task()
# def custom_sum(num1, num2):
#     return num1 + num2


# @shared_task()
# def custom_power(num):
#     if num == 5:
#         raise ValueError('value can not be 5')
#     return num ** 2


# def run_tasks_chain():
#     task_chain = chain(custom_sum.s(2, 3), custom_power.s())
#     task_chain_result = task_chain.apply_async()
#     task_chain_result.get()


# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task()
# def handle_errors_in_dead_letter_queue(*args, **kwargs):
#     print('error has been handled by dead_letter queue')
#
#
# phone_numbers = [
#     '09021234567',
#     '09125469807',
#     '09220986534',
#     '09036578756',
# ]
#
#
# @shared_task()
# def send_sms_to_user(phone_number):
#     if phone_number.startswith('0903'):
#         raise ValueError(f'invalid phone number {phone_number}')
#     else:
#         return f'message has been sent to {phone_number}'
#
#
# def handle_result(result):
#     if result.successful():
#         print(f'Task complete: {result.get()}')
#     elif result.failed() and isinstance(result.result, ValueError):
#         handle_errors_in_dead_letter_queue.apply_async()
#     elif result.status == 'REVOKED':
#         print(f'Task was revoked: {result.id}')
#
#
# def run_tasks_group():
#     task_group = group(send_sms_to_user.s(phone_number) for phone_number in phone_numbers)
#     result_group = task_group.apply_async()
#     result_group.get(disable_sync_subtasks=False, propagate=False)
#     for result in result_group:
#         handle_result(result)
# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task(time_limit=5)
# def send_email_to_user():
#     sleep(6)
#     return "email has been sent to user successfully"
# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task(time_limit=10)
# def send_email_to_user():
#     sleep(6)
#     return "email has been sent to user successfully"
#
#
# def send_email():
#     result = send_email_to_user.apply_async()
#     try:
#         task_result = result.get(timeout=4)
#     except TimeoutError:
#         print('Task timed out')
# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task()
# def my_long_running_task(has_error):
#     if has_error:
#         raise ValueError('an error occurred in long running task')
#     else:
#         sys.stdout.write('long running task has been done')
#
#
# @shared_task()
# def process_result(result):
#     sys.stdout.write('process task result')
#     sys.stdout.flush()
#
#
# @shared_task()
# def process_error_result(task_id, exc, traceback):
#     sys.stdout.write('>>>>>>>>>>>>>>>>>>>')
#     sys.stdout.write(str(exc))
#     sys.stdout.write('>>>>>>>>>>>>>>>>>>>')
#     sys.stdout.flush()
#
#
# def run_task(has_error=False):
#     my_long_running_task.apply_async(args=[has_error], link=[process_result.s()], link_error=[process_error_result.s()])
# -------------------------------------------------------------------------------------------------------------------------------
# @shared_task()
# def my_task():
#     raise ValueError('task failed')
#
#
# @shared_task()
# def error_handler_task(task_id):
#     sys.stdout.write(f'Task id is {task_id}')
#
#
# @task_failure.connect(sender=my_task)
# def handle_my_task_failure(sender=None, task_id=None, **kwargs):
#     error_handler_task.apply_async(args=[task_id])
#
#
# def run_tasks():
#     my_task.apply_async()
# -------------------------------------------------------------------------------------------------------------------------------
