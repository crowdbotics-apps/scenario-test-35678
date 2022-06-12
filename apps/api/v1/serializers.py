from rest_framework import serializers
from apps.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(required=True, max_length=50, min_length=1)
    type = EnumChoiceField(AppTypes, required=True)
    framework = EnumChoiceField(FrameworkTypes, required=True)
    domain_name = models.CharField(max_length=50)
    screenshot = models.CharField(read_only=True)

    class AppTypes(ChoiceEnum):
        web="Web"
        mobile="Mobile"

    class FrameworkTypes(ChoiceEnum):
        django="Django"
        react="React Native"

