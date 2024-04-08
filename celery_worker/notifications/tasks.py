from celery import shared_task


@shared_task()
def send_discount_emails():
    pass


@shared_task()
def process_data_for_machine_learning():
    pass
