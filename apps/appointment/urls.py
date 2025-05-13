from django.urls import path
from .views import professional_schedule_list

urlpatterns = [
    # Schedule
    path('schedule/', professional_schedule_list, name='schedule_list'),
]