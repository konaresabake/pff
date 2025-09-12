from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

class EntiteBudgetee(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom