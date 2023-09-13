from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
import mercadopago
from home.models import Jogo
import datetime
from decouple import config

@login_required
def process_pix(request, id):

    pc = datetime.datetime.now().strftime('%H') #Hora do pc
    game = Jogo.objects.get(id=id) #Hora do jogo começar

    if pc >= game.date.strftime('%H'):
        if game.status == 'Ativo':
            game.status = 'Fechado'
            game.save()
            messages.add_message(request, constants.ERROR, 'Apostas estão encerradas')
            return redirect ('home')
        else:
            messages.add_message(request, constants.ERROR, 'Apostas estão encerradas')
            return redirect ('home')

    if request.method == 'POST':

        valor = float(request.POST.get('valor'))
        escolha = str(request.POST.get('escolha'))
        name = str(request.user)
        email = str(request.user.email)

        print(email)

        payment_data = {
            "transaction_amount": valor,
            "description": f"Aposta no {escolha}",
            "payment_method_id": "pix",
            "payer": {
                "email": "Teste@gmail.com",
                "first_name": name,
                "last_name": "None",
                "identification": {
                    "type": "CPF",
                    "number": "191191191-00"
                },
            }
        } 

        # Processar o pagamento usando o Mercado Pago SDK
        sdk = mercadopago.SDK(config('SDK'))
        payment_response = sdk.payment().create(payment_data)

        pix = payment_response["response"]["point_of_interaction"]["transaction_data"]["ticket_url"]

        return redirect(pix)

        
            
            
