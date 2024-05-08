from django.shortcuts import render
from django.http import HttpResponse
# from .tasks import send_sms


def handle_user_data_sync(request):
    # result = send_sms.apply_async()
    # result.get()
    return HttpResponse("<h1>Hello User sync</h1>")


def handle_user_data_async(request):
    # send_sms.apply_async()
    return HttpResponse("<h1>Hello User async</h1>")
