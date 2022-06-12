from rest_framework import serializers
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    plan = serializers.CharField(required=True)
    app = serializers.CharField(required=True)
    active = serializers.BooleanField(required=True)
