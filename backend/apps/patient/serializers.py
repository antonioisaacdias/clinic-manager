from rest_framework import serializers
from .models import Patient, PlanSubscription

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class PlanSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSubscription
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')
