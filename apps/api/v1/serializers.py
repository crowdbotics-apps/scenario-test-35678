from rest_framework import serializers
from apps.models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"

    name = serializers.CharField(required=True, max_length=50, min_length=1)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(required=True, choices=App.AppTypes)
    framework = serializers.ChoiceField(required=True, choices=App.FrameworkTypes)
    domain_name =  serializers.CharField()
    screenshot =  serializers.URLField(read_only=True)
    subscription = serializers.IntegerField(required=False)
    user = serializers.IntegerField(required=False)

    
