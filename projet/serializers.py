
from rest_framework import serializers
from . import models
class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projet
        fields = "__all__"