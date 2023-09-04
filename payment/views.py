from django.shortcuts import render, redirect
import json
import mercadopago
from decouple import config

def process_pix(request):
    if request.method == 'POST':

        payment_data = {
            "transaction_amount": 100,
            "description": "Título do produto",
            "payment_method_id": "pix",
            "payer": {
                "email": "teste@gmail.com",
                "first_name": "Test",
                "last_name": "User",
                "identification": {
                    "type": "CPF",
                    "number": "191191191-00"
                },
                "address": {
                    "zip_code": "06233-200",
                    "street_name": "Av. das Nações Unidas",
                    "street_number": "3003",
                    "neighborhood": "Bonfim",
                    "city": "Osasco",
                    "federal_unit": "SP"
                }
            }
        } 

        # Processar o pagamento usando o Mercado Pago SDK
        sdk = mercadopago.SDK(config('SDK'))
        payment_response = sdk.payment().create(payment_data)

        pix = payment_response["response"]["point_of_interaction"]["transaction_data"]
        
        

        context = {
            'pix': pix["qr_code_base64"],
            'pix_copiar': pix["qr_code"], 
            
        }

        return render(request, 'payment/payment.html', context)

        # Verificar o status do pagamento e redirecionar com base nisso
        if payment_status == 'approved':
            return redirect('sucesso')  # Substitua 'sucesso' pelo nome da sua rota de sucesso
        else:
            return redirect('home')  # Substitua 'falha' pelo nome da sua rota de falha

    # Se o método da solicitação não for POST, exiba o formulário para o usuário preencher
    return render(request, 'seu_template.html')  # Substitua 'seu_template.html' pelo nome do seu modelo HTML

            
            
