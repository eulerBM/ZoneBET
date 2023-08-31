from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date
from home.models import Jogo

def home(request):

    jogo_do_dia = Jogo.objects.all()

    if request.user.is_authenticated:
        saldo = request.user.user.money
    
    else:
        saldo = 0

    context = {
        'game': jogo_do_dia,  
        'saldo': saldo,         
    }

    return render (request,'home.html', context)

@login_required
def perfil(request):
    return render (request, 'perfil/perfil.html')
