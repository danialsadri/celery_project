from time import sleep
from celery import shared_task


@shared_task()
def send_message(mobile, message):
    sleep(5)
    return f'sms sent to user with {mobile} number and message was: {message}'
