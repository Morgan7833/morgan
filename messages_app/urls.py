from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('', views.message_list, name='list'),
    path('send/', views.send_message, name='send'),
    path('poll/', views.poll_messages, name='poll'),
]



