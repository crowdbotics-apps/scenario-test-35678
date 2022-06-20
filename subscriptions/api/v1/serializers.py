#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Apps Serializer Class.
The  Serializer class describes how the request and response of the application  will look like
as well as the constraints

* Author: Mahmoud Ibrahim
* Date: 20/6/2022
"""


from rest_framework import serializers
from apps.models import App
from plans.models import Plan
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """App Serializer Class that describes the API request and response.
    """

    class Meta:
        model = Subscription
        fields = "__all__"

    # user FK
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    # plan FK
    plan = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Plan.objects.all())

    # app FK
    app = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=App.objects.all())

    # Subscription status
    active = serializers.BooleanField(required=True)
