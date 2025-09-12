
from rest_framework import serializers
from . import models
class RessourceHumaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RessourceHumaine
        fields = "__all__"