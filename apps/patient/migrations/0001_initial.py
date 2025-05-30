# Generated by Django 5.2 on 2025-04-18 00:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPacient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não informado'), ('O', 'Outro')], max_length=1)),
                ('plan_card', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('guardian_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
