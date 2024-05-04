from django.urls import path
from . import views

app_name = 'notifications'
urlpatterns = [
    path('sync/', views.handle_user_data_sync, name='handle_user_data_sync'),
    path('async/', views.handle_user_data_async, name='handle_user_data_async'),
]
