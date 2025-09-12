
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r"utilisateurs", views.UtilisateurViewSet)
urlpatterns = [
    path('', include(router.urls)), 
    ]
# from django.contrib import admin
# from django.contrib.auth import get_user_model


# User = get_user_model()
# @admin.register(User)
# class UtilisateurAdmin(admin.ModelAdmin):
#     list_display = ("username", "email", "role", "is_staff", "is_superuser")
#     list_filter = ("role", "is_staff", "is_superuser")
#     search_fields = ("username", "email")
