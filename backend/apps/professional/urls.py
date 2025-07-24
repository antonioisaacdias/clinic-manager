from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, SpecialtyViewSet

router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet, basename='professional')
router.register(r'specialties', SpecialtyViewSet, basename='specialty')

urlpatterns = [
    path('', include(router.urls)),
]