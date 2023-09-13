from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from home.utils import user_on
from django.contrib.auth.models import User


@login_required
def perfil(request):

    if request.method == 'POST':
        nome1 = str(request.POST.get('nome1')).capitalize()
        nome2 = str(request.POST.get('nome2')).capitalize()

        if nome1 == '':
            messages.add_message(request, constants.ERROR, 'Por favor, preencha o primeiro nome tambem!')
            return redirect ('perfil')

        elif nome2 == '':
            messages.add_message(request, constants.ERROR, 'Por favor, preencha o sobrenome tambem!')
            return redirect ('perfil')

        if not request.user.first_name and not request.user.last_name:
            if not User.objects.filter(first_name=nome1):
                request.user.first_name = nome1
                request.user.last_name = nome2
                request.user.save()
                messages.add_message(request, constants.SUCCESS, 'Dados salvos')
                return redirect ('perfil')
            
            else:
                messages.add_message(request, constants.ERROR, 'Esse nome esta em uso')
                return redirect ('perfil')
        else:
            messages.add_message(request, constants.ERROR, 'Erro')
            return redirect ('perfil')


    if request.method == 'GET':

        saldo = user_on(request.user)

        context = { 
            'saldo': saldo,
        

        }
        return render (request, 'perfil/perfil.html', context)
    
    

        
