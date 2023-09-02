from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from home.models import Jogo

class aposta(models.Model):
    choices_status = (
        ('Ativo', 'Ativo'),
        ('Em jogo', 'Em jogo'),
        ('Fechado', 'Fechado'),
    )

    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=50)
    valor = MoneyField(default=0 ,max_digits=10, decimal_places=2, default_currency='BRL')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Apostou!"
