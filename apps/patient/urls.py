from django.urls import path
from .views import PatientCreateView, PatientListView, PatientUpdateView, PatientDetailView, PatientDeleteView

urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('<uuid:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<uuid:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('<uuid:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('', PatientListView.as_view(), name='patient_list'),
]

