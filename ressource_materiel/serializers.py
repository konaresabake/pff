
from rest_framework import serializers
from . import models

class RessourceMaterielleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RessourceMaterielle
        fields = "__all__"