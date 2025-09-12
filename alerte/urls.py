from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'alertes', views.AlerteViewSet, basename='alerte')

urlpatterns = [
    path('', include(router.urls)),
]