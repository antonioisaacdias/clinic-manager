from django.urls import path
from .views import today_appointments_view, calendar_events

urlpatterns = [
    path('', today_appointments_view, name='appointment_today'),
    path('api/appointments/', calendar_events, name='calendar_events'),
    
]