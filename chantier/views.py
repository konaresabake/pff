from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions

# class IsAdminOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff

# Create your views here.
class ChantierViewSet(viewsets.ModelViewSet):
    queryset = models.Chantier.objects.all()
    serializer_class = serializers.ChantierSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["projet", "statut"]