from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
class RessourceHumaineViewSet(viewsets.ModelViewSet):
    queryset = models.RessourceHumaine.objects.all()
    serializer_class = serializers.RessourceHumaineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
