from django.conf import settings
from django.db import models


class Plan(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.TextField(
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
