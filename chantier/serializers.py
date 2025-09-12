
from rest_framework import serializers
from . import models
class ChantierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chantier
        fields = "__all__"