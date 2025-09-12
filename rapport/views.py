from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
class RapportViewSet(viewsets.ModelViewSet):
    queryset = models.Rapport.objects.all()
    serializer_class = serializers.RapportSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["chantier"]