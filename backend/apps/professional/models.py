from django.db import models
import uuid


class Professional(models.Model):
    gender_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='professionals/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add_specialty(self, specialty):
        self.specialties.add(specialty)

    def remove_specialty(self, specialty):
        self.specialties.remove(specialty)
    
    def list_specialties(self):
        specialties = self.specialties.all()

        specialties_data = []
        for specialty in specialties:
            specialties_data.append({
                'uuid': str(specialty.uuid),
                'name': specialty.name,
            })
        return specialties_data

    def __str__(self):
        return self.name

class Specialty(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    professionals = models.ManyToManyField('Professional', related_name='specialties', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


