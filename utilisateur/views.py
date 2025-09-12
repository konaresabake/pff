from django.shortcuts import render

from rest_framework import viewsets, permissions, filters
from django.contrib.auth.models import User
from . import models
from . import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UtilisateurSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["username", "email", "first_name", "last_name"]