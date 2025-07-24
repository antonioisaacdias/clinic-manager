from django.urls import path
from .views import PlanViewSet 
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'plans', PlanViewSet, basename='plan')

urlpatterns = [
    path('', include(router.urls)),
]