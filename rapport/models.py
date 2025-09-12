from django.db import models
from chantier.models import Chantier

# Create your models here.
class Rapport(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE, related_name="rapports", null=True, blank=True)
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def generer_pdf(self):
        # placeholder pour génération PDF (à implémenter)
        return f"/rapports/{self.pk}.pdf"

    def __str__(self):
        return self.titre
