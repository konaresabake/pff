from django.db import models
from entite_budget.models import EntiteBudgetee

# Create your models here.
class Projet(models.Model):
    entite = models.ForeignKey(EntiteBudgetee, on_delete=models.CASCADE, related_name="projets")
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=50, default="planifié")

    def demarrer(self):
        self.statut = "en cours"
        self.save(update_fields=["statut"])

    def cloturer(self):
        self.statut = "clos"
        self.save(update_fields=["statut"])

    def __str__(self):
        return self.nom