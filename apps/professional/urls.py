from django.urls import path
from .views import SpecialtyListView, SpecialtyCreateView
urlpatterns = [
    path('specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty_create')
]