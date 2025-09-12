from django.db import models
from projet.models import Projet

# Create your models here.
class Chantier(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="chantiers")
    nom = models.CharField(max_length=200)
    localisation = models.CharField(max_length=255, blank=True)
    responsable = models.CharField(max_length=200, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=50, default="fermé")

    def ouvrir(self):
        self.statut = "ouvert"
        self.save(update_fields=["statut"])

    def fermer(self):
        self.statut = "fermé"
        self.save(update_fields=["statut"])

    def __str__(self):
        return f"{self.nom} ({self.projet.nom})"