from django.db import models
from chantier.models import Chantier


# Create your models here.
class Alerte(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE, related_name="alerte", null=True, blank=True)
    categorie = models.CharField(max_length=100)
    description = models.TextField()
    priorite = models.IntegerField(default=1)
    date_declenchement = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def declencher(self):
        self.active = True
        self.save(update_fields=["active"])

    def __str__(self):
        return f"{self.categorie} - p{self.priorite}"