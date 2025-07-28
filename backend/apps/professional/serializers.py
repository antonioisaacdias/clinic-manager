from rest_framework import serializers
from .models import Professional, Specialty

class ProfessionalSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Professional
        fields = ['uuid', 'name', 'photo', 'photo_url', 'gender', 'is_active', 'email', 'phone', 'cpf', 'rg', 'address', 'birth_date']
        read_only_fields = ('created_at', 'updated_at')

    def get_photo_url(self, obj):
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
        read_only_fields = ('created_at', 'updated_at')