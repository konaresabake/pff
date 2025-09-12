from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers
class RessourceViewSet(viewsets.ModelViewSet):
    queryset = models.Ressource.objects.all()
    serializer_class = serializers.RessourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["tache", "fournisseur"]

# Create your views here.
