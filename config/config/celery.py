import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

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
    'notifications.tasks.task_1': {'queue': 'default'},
    'notifications.tasks.task_2': {'queue': 'default'},
    'notifications.tasks.task_3': {'queue': 'default'},
    'notifications.tasks.task_4': {'queue': 'default'},
}

app.autodiscover_tasks()
