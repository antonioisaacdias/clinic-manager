from rest_framework import viewsets
from .models import Patient, PlanSubscription
from .serializers import PatientSerializer, PlanSubscriptionSerializer
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'uuid'

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.get_serializer(patient)
        plans_subscriptions = patient.plan_subscriptions.filter(is_active=True)
        subscription_data = []
        for plan_subscription in plans_subscriptions:
            subscription_data.append({
                'uuid': str(plan_subscription.uuid),
                'plan_name': plan_subscription.plan.name,
                'plan_number': plan_subscription.plan_number,
            })
        return Response({
            'patient': serializer.data,
            'plan_subscriptions': subscription_data
        })


class PlanSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = PlanSubscription.objects.all()
    serializer_class = PlanSubscriptionSerializer
    lookup_field = 'uuid'
