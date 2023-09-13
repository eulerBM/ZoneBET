from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from home.models import Jogo

class aposta(models.Model):

    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=50)
    método = models.CharField(max_length=50)
    valor = MoneyField(default=0 ,max_digits=10, decimal_places=2, default_currency='BRL')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} Apostou!"

    def save(self, *args, **kwargs):
        # Verifique se já existe uma aposta do mesmo usuário para o mesmo jogo
        existing_bet = aposta.objects.filter(jogo=self.jogo, user=self.user).first()
        
        if not existing_bet:
            super(aposta, self).save(*args, **kwargs)
        else:  
            raise Exception("Este usuário já fez uma aposta para este jogo.")