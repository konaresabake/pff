from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
class TacheViewSet(viewsets.ModelViewSet):
    queryset = models.Tache.objects.all()
    serializer_class = serializers.TacheSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["lot", "statut"]
