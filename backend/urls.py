from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from backend.swaggers import schema_view




urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("utilisateur.urls")),
    path("api/", include("alerte.urls")),
    path("api/", include("fournisseur.urls")),
    path("api/", include("projet.urls")),
    path("api/", include("chantier.urls")),
    path("api/", include("lot.urls")),
    path("api/", include("tache.urls")),
    path("api/", include("ressource.urls")),
    path("api/", include("ressource_humain.urls")),
    path("api/", include("ressource_materiel.urls")),
    path("api/", include("budget.urls")),
    path("api/", include("entite_budget.urls")),
    path("api/", include("rapport.urls")),
    path("api/", include("django.contrib.auth.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # JWT endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
