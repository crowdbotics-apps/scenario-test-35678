from django.conf import settings
from django.db import models


class Subscription(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
    )
    plan = models.ForeignKey(
        "plans.Plan",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_plan",
    )
    app = models.ForeignKey(
        "apps.App",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_app",
    )
    active = models.BooleanField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


# Create your models here.
