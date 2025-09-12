from django.db import models
from ressource.models import Ressource

# Create your models here.
class RessourceHumaine(models.Model):
    ressource = models.OneToOneField(Ressource, on_delete=models.CASCADE, related_name="humaine")
    qualification = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Humain: {self.ressource.nom}"