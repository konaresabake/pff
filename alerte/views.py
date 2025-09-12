from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
class AlerteViewSet(viewsets.ModelViewSet):
    queryset = models.Alerte.objects.all()
    serializer_class = serializers.AlerteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["chantier", "categorie", "active"]
