from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.

class RessourceMaterielleViewSet(viewsets.ModelViewSet):
    queryset = models.RessourceMaterielle.objects.all()
    serializer_class = serializers.RessourceMaterielleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]