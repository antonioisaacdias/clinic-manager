from django.urls import path
from .views import ModelAppointmentListView, ModelAppointmentUpdateView

urlpatterns = [
    path('', ModelAppointmentListView.as_view(), name='appointment_today'),
    path('<uuid:pk>/update/', ModelAppointmentUpdateView.as_view(), name='appointment_update'),
    
]