
from rest_framework import serializers 
from . import models

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tache
        fields = "__all__"