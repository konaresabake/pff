from django.db import models

from lot.models import Lot



# from lot.models import Lot

# Create your models here.
class Tache(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name="taches", null=True, blank=True)
    intitule = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    avancement = models.FloatField(default=0.0)
    statut = models.CharField(max_length=50, default="à faire")

    def commencer(self):
        self.statut = "en cours"
        self.save(update_fields=["statut"])

    def terminer(self):
        self.statut = "terminée"
        self.avancement = 100.0
        self.save(update_fields=["statut", "avancement"])

    def __str__(self):
        return self.intitule