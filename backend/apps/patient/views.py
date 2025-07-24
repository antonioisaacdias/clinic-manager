from rest_framework import viewsets
from .models import Patient, PlanSubscription
from .serializers import PatientSerializer, PlanSubscriptionSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PlanSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = PlanSubscription.objects.all()
    serializer_class = PlanSubscriptionSerializer
