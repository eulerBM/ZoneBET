from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.utils import user_on
from home.models import Jogo
from aposta.models import aposta

@login_required
def page_aposta(request, id):

    if request.method == 'GET':
        saldo = user_on(request.user)

        game = Jogo.objects.get(id=id)

        context = { 
            'saldo': saldo,
            'game': game,
            
        }
        return render (request, 'aposta/aposta.html', context)
    
    else:
        print(request.POST)
        game = Jogo.objects.get(id=id)

        create_aposta = aposta.objects.create(
            jogo=game,
            escolha=request.POST.get('escolha'),
            valor=request.POST.get('valor'),
            user=request.user,

        )

        return redirect('home')
       

