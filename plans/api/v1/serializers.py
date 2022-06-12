from rest_framework import serializers
from plans.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


    name = serializers.CharField(required=True, max_length=20, min_length=1)
    description = serializers.CharField(required=True, min_length=1)

