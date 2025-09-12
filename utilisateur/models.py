from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Utilisateur(AbstractUser):
    ROLE_ADMIN = "admin"
    ROLE_MAITRE = "maitre_ouvrage"
    ROLE_CHEF = "chef_projet"
    ROLE_MEMBRE = "membre_technique"
    ROLE_CHOICES = [
        (ROLE_ADMIN, "Administrateur"),
        (ROLE_MAITRE, "MaitreOuvrage"),
        (ROLE_CHEF, "ChefProjet"),
        (ROLE_MEMBRE, "MembreTechnique"),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=ROLE_MEMBRE)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"