from rest_framework import serializers
from apps.models import App
from enum import Enum


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"

    class AppTypes(Enum):
        web="Web"
        mobile="Mobile"

    class FrameworkTypes(Enum):
        django="Django"
        react="React Native"


    id = serializers.UUIDField(primary_key=True, editable=False, unique=True)
    name = serializers.CharField(required=True, max_length=50, min_length=1)
    type = serializers.numChoiceField(AppTypes, required=True)
    framework = serializers.EnumChoiceField(FrameworkTypes, required=True)
    domain_name = serializers.CharField(max_length=50)
    screenshot = serializers.CharField(read_only=True)

    
