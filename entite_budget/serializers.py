from rest_framework import serializers
from . import models


class EntiteBudgeteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntiteBudgetee
        fields = "__all__"