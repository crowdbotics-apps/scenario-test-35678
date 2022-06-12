from django.conf import settings
from django.db import models


class Subscription(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
    )


# Create your models here.
