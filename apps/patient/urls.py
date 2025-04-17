from django.urls import path
from .views import PatientCreateView, PatientListView, PatientUpdateView

urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('<uuid:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('', PatientListView.as_view(), name='patient_list')
]

