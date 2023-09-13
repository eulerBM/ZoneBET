from django.shortcuts import render
from home.models import Jogo
from home.utils import user_on
import datetime


def home(request):
    jogo_do_dia = Jogo.objects.all().order_by('-date')[:8]
    
    saldo = user_on(request.user)

    context = {
        'game': jogo_do_dia,  
        'saldo': saldo,         
    }

    return render (request,'home.html', context)




