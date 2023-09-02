from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.utils import user_on


@login_required
def perfil(request):

    saldo = user_on(request.user)

    context = { 
        'saldo': saldo,

    }
    return render (request, 'perfil/perfil.html', context)
