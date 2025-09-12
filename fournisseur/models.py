from django.db import models


# Create your models here.
class Fournisseur(models.Model):
    nom = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True)
    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)

    def fournir_ressource(self, ressource, quantite):
        # placeholder logique métier : à implémenter selon besoin
        return True

    def __str__(self):
        return self.nom