from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class ModelSpecialty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)


class ModelProfessional(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não informado'),
        ('O', 'Outro'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)
    registration_number = models.CharField(blank=True, null=True, max_length=30)
    phone = models.CharField(max_length=11)
    specialties = models.ManyToManyField(ModelSpecialty, related_name='professionals')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional_profile')
    
    def get_gender_display_label(self):
        return dict(self.GENDER_CHOICES).get(self.gender, 'Desconhecido')
    
