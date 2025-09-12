from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'fournisseurs', views.FournisseurViewSet, basename='fournisseur')

urlpatterns = [
    path('', include(router.urls)),
]