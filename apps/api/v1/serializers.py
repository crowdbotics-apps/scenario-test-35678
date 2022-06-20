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
import logging

from subscriptions.models import Subscription


class AppSerializer(serializers.ModelSerializer):
    """App Serializer Class that describes the API request and response.
    """

    logger = logging.getLogger(__name__)

    class Meta:
        model = App
        fields = "__all__"

    # API requests and responses specifications
    # application name which is required and its max and  min length
    name = serializers.CharField(required=True, max_length=50, min_length=1)

    # description fieild which is optional
    description = serializers.CharField(required=False)

    # type of the application which is an ENUM value based on the  model
    type = serializers.ChoiceField(required=True, choices=App.AppTypes)

    # Framework type for the application type
    framework = serializers.ChoiceField(required=True, choices=App.FrameworkTypes)

    # the appliaction domain name which is optional
    domain_name = serializers.CharField(required=False)

    # screeshot of the application which is a ready only field
    screenshot = serializers.URLField(read_only=True)

    # subscription id which gets the apps subscription plane
    subscription = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    # application owner which is read only and PK
    user = serializers.PrimaryKeyRelatedField(read_only=True)
