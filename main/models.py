from django.db import models
from django.contrib.auth.models import AbstractUser
from main.OAuth import oauthModels

class User(AbstractUser):
    access_key = models.ForeignKey(oauthModels.AccessKey, on_delete=models.CASCADE, null=True, blank=True)

class GoogleAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Script(models.Model):
    context = models.TextField(max_length=5000, null=True, blank=True)
    language = models.CharField(max_length=150, null=True, blank=True)


