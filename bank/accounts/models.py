from django.db import models
from datetime import datetime

# Create your models here.

class Account(models.Model):
    owner = models.CharField(max_length=50)
    balance = models.FloatField()
    creation_date = models.DateTimeField(default=datetime.now())