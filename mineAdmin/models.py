from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserStat(models.Model):
    month = models.CharField(max_length=20)
    avg_users = models.FloatField()
    avg_new_users = models.FloatField()


class Mod(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=1024)
    url = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
