from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
class ProjetViewSet(viewsets.ModelViewSet):
    queryset = models.Projet.objects.all()
    serializer_class = serializers.ProjetSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["entite", "statut"]