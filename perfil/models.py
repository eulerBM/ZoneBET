from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

class dados(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = MoneyField(default=0 ,max_digits=10, decimal_places=2, default_currency='BRL')

    def __str__(self):
        return f"{self.user} {self.money}"