from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from django.db import models

class Jogo(models.Model):
    choices_status = (
        ('Ativo', 'Ativo'),
        ('Em jogo', 'Em jogo'),
        ('Fechado', 'Fechado'),
    )

    team1 = models.CharField(max_length=60, blank=False, verbose_name='Time 1')
    team2 = models.CharField(max_length=60, blank=False, verbose_name='Time 2')
    status = models.CharField(choices=choices_status, blank=False, max_length=8 , verbose_name='Status')
    date = models.DateTimeField(blank=False, verbose_name='Data do evento')

    def __str__(self):
        return f"{self.team1} X {self.team2}"

class user_money(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = MoneyField(max_digits=10, decimal_places=2, default_currency='BRL')

    def __str__(self):
        return f"{self.user} {self.money}"