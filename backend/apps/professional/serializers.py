from rest_framework import serializers
from .models import Professional, Specialty

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')