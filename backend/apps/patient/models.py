from django.db import models
import uuid


class Patient(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='patients/photos/', blank=True, null=True)

    need_guardian = models.BooleanField(default=False)
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_cpf = models.CharField(max_length=11, blank=True, null=True)
    guardian_phone = models.CharField(max_length=15, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_active_plan_subscriptions(self):
        plans_subscriptions = self.plan_subscriptions.filter(is_active=True)

        plan_details = []

        for subscription in plans_subscriptions:
            plan_details.append({
                'plan_uuid': subscription.plan.uuid,
                'plan_name': subscription.plan.name,
            })

        return plan_details
    
    def add_plan_subscrption(self, plan_subscription):
        plan_subscription.patient = self
        plan_subscription.save()
        return plan_subscription

class PlanSubscription(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='plan_subscriptions', blank=True, null=True)
    plan = models.ForeignKey('administration.Plan', on_delete=models.CASCADE)
    plan_number = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['patient', 'plan'],
                condition=models.Q(is_active=True),
                name='unique_active_plan_subscription'
            )
        ]

    def __str__(self):
        return f"{self.patient.name} - {self.plan.name}"

