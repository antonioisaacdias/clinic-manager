from django.urls import path
from .views import SpecialtyListView, SpecialtyCreateView, SpecialtyDetailView, SpecialtyUpdateView, change_specialty_activity_view
urlpatterns = [
    path('specialties/', SpecialtyListView.as_view(), name='specialty_list'),
    path('specialties/<uuid:pk>/', SpecialtyDetailView.as_view(), name='specialty_detail'),
    path('specialties/<uuid:pk>/update/', SpecialtyUpdateView.as_view(), name='specialty_update'),
    path('specialties/<uuid:pk>/active/', change_specialty_activity_view, name='specialty_active'),
    path('specialties/create/', SpecialtyCreateView.as_view(), name='specialty_create')
]