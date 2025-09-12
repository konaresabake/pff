
from rest_framework import serializers
from . import models
class AlerteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alerte
        fields = "__all__"