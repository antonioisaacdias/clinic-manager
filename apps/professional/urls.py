from django.urls import path
from .views import SpecialtyListView, SpecialtyCreateView, SpecialtyDetailView, SpecialtyUpdateView
urlpatterns = [
    path('specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('specialties/<uuid:pk>/', SpecialtyDetailView.as_view(), name='specialty_detail'),
    path('specialties/<uuid:pk>/update/', SpecialtyUpdateView.as_view(), name='specialty_update'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty_create')
]