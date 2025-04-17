from django.urls import path
from .views import PatientCreateView, PatientListView

urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('', PatientListView.as_view(), name='patient_list')
]

