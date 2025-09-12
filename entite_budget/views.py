from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions, filters
from . import models
from . import serializers
class EntiteBudgeteeViewSet(viewsets.ModelViewSet):
    queryset = models.EntiteBudgetee.objects.all()
    serializer_class = serializers.EntiteBudgeteeSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nom", "description"]
    