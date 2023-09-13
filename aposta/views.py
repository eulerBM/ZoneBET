from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.utils import user_on
from home.models import Jogo
from aposta.models import aposta
from django.contrib import messages
from django.contrib.messages import constants
from aposta.forms import form_aposta, form_validação
import datetime


hora_atual = datetime.datetime.now().strftime('%H')

hora_atual = datetime.datetime.now().strftime('%H')


@login_required
def page_aposta(request, id):
    game = Jogo.objects.get(id=id)
    

    if game.date.strftime('%H') < hora_atual:
        messages.add_message(request, constants.ERROR, 'O jogo ja começou, apostas estão encerradas!')

        return redirect('home')

    if request.method == 'GET':

        saldo = user_on(request.user)


        context = { 
            'saldo': saldo,
            'game': game,
            'form': form_aposta(times=[game.team1, 'Empate', game.team2]),   
            'erro': form_validação.errors,     
        }

        return render (request, 'aposta/aposta.html', context)
    
    else:
        form = form_validação(request.POST)

        if form.is_valid():

            
            
            aposta.objects.create(
                    jogo=game,
                    escolha=form.cleaned_data['escolha'],
                    método=form.cleaned_data['metodo'],
                    valor=form.cleaned_data['valor'],
                    user=request.user
                )

            return redirect('home')  
            

        else:
            messages.add_message(request, constants.ERROR, form.errors)
            return redirect('aposta', id)
       

