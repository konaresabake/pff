from django.db import models
from ressource.models import Ressource

# Create your models here.
class RessourceMaterielle(models.Model):
    ressource = models.OneToOneField(Ressource, on_delete=models.CASCADE, related_name="materielle")
    caracteristique = models.TextField(blank=True)

    def __str__(self):
        return f"Matériel: {self.ressource.nom}"