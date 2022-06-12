from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    type = models.TextField(
        null=True,
        blank=True,
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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="app_subscription",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="app_user",
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
