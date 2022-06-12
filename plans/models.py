from django.conf import settings
from django.db import models


class Plan(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.TextField(
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
