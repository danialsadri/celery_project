import logging
import os
from celery import Celery, Task
from kombu import Exchange, Queue


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('connection error occurred in project')
        else:
            print(f'task id: {task_id} got error')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.Task = CustomTask

app.conf.update(
    task_acks_late=True,
    task_default_priority=5,
    worker_prefetch_multiplier=1,
    worker_concurrency=1)

default_exchange = Exchange(name='default', type='direct')
app.conf.task_queues = (
    Queue(name='default', exchange=default_exchange, routing_key='default', queue_arguments={'x-max-priority': 10}),
)
task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'

app.conf.task_routes = {
    'notifications.tasks.task_test.task_1': {'queue': 'default'},
    'notifications.tasks.task_test.task_2': {'queue': 'default'},
    'notifications.tasks.task_test.task_3': {'queue': 'default'},
    'notifications.tasks.task_test.task_4': {'queue': 'default'},
    'notifications.tasks.task_send_message.send_message': {'queue': 'default'},
    'notifications.tasks.task_send_sms.send_sms': {'queue': 'default'},
    'notifications.tasks.task_raise_error.raise_error_1': {'queue': 'default'},
    'notifications.tasks.task_raise_error.raise_error_2': {'queue': 'default'},
    'notifications.tasks.task_raise_error.raise_error_3': {'queue': 'default'},
    'notifications.tasks.task_raise_error.send_sms_to_user': {'queue': 'default'},
    'notifications.tasks.task_raise_error.custom_sum': {'queue': 'default'},
    'notifications.tasks.task_raise_error.custom_power': {'queue': 'default'},
}

app.autodiscover_tasks()
