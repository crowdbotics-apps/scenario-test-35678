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
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscription_plan",
    )
    app = models.ForeignKey(
        "apps.App",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="subscription_app",
    )
    active = models.BooleanField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )


# Create your models here.
