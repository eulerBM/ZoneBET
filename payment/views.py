from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import mercadopago
from decouple import config

@login_required
def process_pix(request):
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

        
            
            
