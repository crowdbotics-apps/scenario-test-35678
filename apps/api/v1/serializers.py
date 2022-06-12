from rest_framework import serializers
from apps.models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"

    name = serializers.CharField(required=True, max_length=50, min_length=1)
    type = serializers.CharField(required=True)
    framework = serializers.CharField(required=True)
    domain_name = serializers.CharField(max_length=50)

    
