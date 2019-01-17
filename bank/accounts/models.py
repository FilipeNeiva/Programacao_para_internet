from django.db import models

# Create your models here.
from django.utils import timezone


class Account(models.Model):
    owner = models.CharField(max_length=50)
    balance = models.FloatField()
    creation_date = models.DateTimeField()

    def credit(self, valor):
        self.balance = self.balance - valor

    def debit(self, valor):
        self.balance = self.balance + valor
