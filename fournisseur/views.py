from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, filters
from . import models
from . import serializers


class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = models.Fournisseur.objects.all()
    serializer_class = serializers.FournisseurSerializer
    permission_classes = [permissions.AllowAny]
