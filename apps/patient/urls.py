from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_patient_view, name='create_pacient')
]