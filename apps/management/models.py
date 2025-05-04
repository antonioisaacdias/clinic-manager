from django.db import models
from uuid import uuid4

class ModelPlan(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name