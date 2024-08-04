from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **kwargs):
        if not email:
            raise ValueError("Un e-mail doit être renseigné")
        if not first_name:
            raise ValueError("Un prénom doit être renseigné")
        if not last_name:
            raise ValueError("Un nom doit être renseigné")

        email = self.normalize_email(email)
        first_name = first_name.strip().capitalize()
        last_name = last_name.strip().upper()

        user = self.model(email=email, first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Pour faire partie du staff, l'utilisateur doit avoir is_staff=True")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Pour faire partie des administrateurs, l'utilisateur doit avoir is_superuser=True")

        return self.create_user(email, first_name, last_name, password, **kwargs)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Adresse e-mail", max_length=128, unique=True)
    first_name = models.CharField(verbose_name="Prénom", max_length=64, blank=False)
    last_name = models.CharField(verbose_name="Nom", max_length=64, blank=False)
    password = models.CharField(verbose_name="Mot de passe", max_length=128)
    last_login = models.DateTimeField(verbose_name="Date de la dernière connexion", blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name="Date d'inscription", default=timezone.now)
    is_active = models.BooleanField(verbose_name="Status d'activation", default=True)
    is_staff = models.BooleanField(verbose_name="Staff", default=False)
    is_superuser = models.BooleanField(verbose_name="Administrateur", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
