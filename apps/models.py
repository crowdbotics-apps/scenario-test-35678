from django.conf import settings
from django.db import models



class App(models.Model):
    "Generated Model"

    AppTypes = (
            ("Web", "Web Application"),
            ("Mobile", "Mobile Application"),
    )

    FrameworkTypes = (
            ("Django", "Django Framework"),
            ("React Native", "React Native Framework"),
    )

    name = models.TextField(
        null=False,
        blank=False,
    )
    description = models.TextField(
         null=True,
        blank=True,
    )
    type = models.TextField(
        null=False,
        blank=False,
        choices=AppTypes,
    )
    framework = models.TextField(
        null=True,
        blank=True,
        choices=FrameworkTypes,
    )
    domain_name = models.TextField(
        null=True,
        blank=True,
    )
    screenshot = models.FileField(
    )
    subscription = models.ForeignKey(
        "subscriptions.Subscription",
        on_delete=models.SET_NULL,
        related_name="app_subscription",
    )
    user = models.ForeignKey(
        "users.User",
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