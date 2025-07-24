from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PlanSubscriptionViewSet
from django.urls import include

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'plan-subscriptions', PlanSubscriptionViewSet, basename='plan-subscription')

urlpatterns = [
    path('', include(router.urls)),
]