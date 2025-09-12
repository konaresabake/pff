
from rest_framework import serializers
from . import models
class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ressource
        fields = "__all__"