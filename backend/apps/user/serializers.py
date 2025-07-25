from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField()
        self.fields['password'] = serializers.CharField()
        self.fields.pop('username', None)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.first_name or user.username
        token['email'] = user.email
        token['username'] = user.username
        return token
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
                
            if user is None:
                raise serializers.ValidationError({
                    'detail': 'Credenciais inválidas.'
                })
            if not user.is_active:
                raise serializers.ValidationError({
                    'detail': 'Conta desativada.'
                })
        else:
            raise serializers.ValidationError({
                'detail': 'Email e senha são obrigatórios.'
            })
        
        attrs['username'] = user.username
        
        return super().validate(attrs)