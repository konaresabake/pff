from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, BasePermission
from . import models
from .serializers import BudgetSerializer
from rest_framework import permissions

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = models.Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["entite"]
