from django.db import models
from chantier.models import Chantier

# Create your models here.
class Lot(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE, related_name="lots", null=True, blank=True)
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)

    def planifier(self, start, end):
        self.date_debut = start
        self.date_fin = end
        self.save(update_fields=["date_debut", "date_fin"])

    def __str__(self):
        return self.nom