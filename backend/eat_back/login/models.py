from django.db import models

# Create your models here.
from django.db import models


class Account(models.Model):
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    userid = models.CharField(max_length=20)
