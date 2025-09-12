
from rest_framework import serializers
from . import models
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fournisseur
        fields = "__all__"