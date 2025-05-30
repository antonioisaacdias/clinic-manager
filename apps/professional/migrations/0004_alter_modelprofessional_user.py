# Generated by Django 5.2 on 2025-05-09 02:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0003_modelprofessional_is_active_modelspecialty_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelprofessional',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professional_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
