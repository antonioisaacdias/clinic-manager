from rest_framework import serializers
from .models import Professional, Specialty

class ProfessionalSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Professional
        fields = ['uuid', 'name', 'specialties', 'photo']
        read_only_fields = ('created_at', 'updated_at', 'is_active')

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo:
            url = obj.photo.url
            if request is not None:
                return request.build_absolute_uri(url)
            return url
        return None

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_active')