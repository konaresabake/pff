from django.db import models
from fournisseur.models import Fournisseur
from tache.models import Tache

# Create your models here.
class Ressource(models.Model):
    tache = models.ForeignKey(Tache, on_delete=models.SET_NULL, related_name="ressources", null=True, blank=True)
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=100, blank=True)
    quantite = models.FloatField(default=0.0)
    unite = models.CharField(max_length=50, blank=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True, related_name="ressources")

    def __str__(self):
        return f"{self.nom} ({self.quantite} {self.unite})"