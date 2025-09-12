from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'lots', views.LotViewSet, basename='lot')

urlpatterns = [
    path('', include(router.urls)),
]