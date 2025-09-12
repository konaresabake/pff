from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from . import models
from . import serializers


class LotViewSet(viewsets.ModelViewSet):
    queryset = models.Lot.objects.all()
    serializer_class = serializers.LotSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["chantier"]

# Create your views here.
