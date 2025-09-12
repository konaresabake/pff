from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r"entites", views.EntiteBudgeteeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
