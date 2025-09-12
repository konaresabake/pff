
from rest_framework import serializers
from . import models
class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lot
        fields = "__all__"