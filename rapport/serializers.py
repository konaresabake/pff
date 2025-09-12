
from rest_framework import serializers
from . import models
class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rapport
        fields = "__all__"