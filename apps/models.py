from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.TextField(
        null=False,
        blank=False,
    )
    description = models.TextField()
    type = models.TextField(
        null=False,
        blank=False,
    )
    framework = models.TextField(
        null=True,
        blank=True,
    )
    domain_name = models.TextField(
        null=True,
        blank=True,
    )
    screenshot = models.TextField(
        null=True,
        blank=True,
    )
    subscription = models.ForeignKey(
        "subscriptions.Subscription",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="app_subscription",
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="app_user",
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
