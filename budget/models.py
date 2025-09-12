from django.db import models
from entite_budget.models import EntiteBudgetee


# Create your models here.
class Budget(models.Model):
    entite = models.ForeignKey(EntiteBudgetee, on_delete=models.CASCADE, related_name="budgets")
    montant_initial = models.FloatField()
    cout_reel = models.FloatField(default=0.0)
    reste_a_payer = models.FloatField(default=0.0)

    def ajuster_montant(self, delta: float):
        self.cout_reel += float(delta)
        self.reste_a_payer = max(0.0, self.montant_initial - self.cout_reel)
        self.save(update_fields=["cout_reel", "reste_a_payer"])

    def __str__(self):
        return f"Budget {self.pk} - {self.entite.nom}"