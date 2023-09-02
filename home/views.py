from django.shortcuts import render
from home.models import Jogo
from home.utils import user_on

def home(request):

    jogo_do_dia = Jogo.objects.all()

    saldo = user_on(request.user)

    context = {
        'game': jogo_do_dia,  
        'saldo': saldo,         
    }

    return render (request,'home.html', context)




