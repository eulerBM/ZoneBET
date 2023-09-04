from django import forms
from django.core.exceptions import ValidationError
from djmoney.forms import MoneyWidget
from djmoney.money import Money
from aposta.models import *
       
# Form da aposta
class form_aposta(forms.Form):
    def __init__(self, *args, **kwargs):
        times = kwargs.pop('times', [])
        super(form_aposta, self).__init__(*args, **kwargs)

        self.fields['escolha'] = forms.ChoiceField(
            choices=[(time, time) for time in times],
            required=True,
            widget=forms.Select(attrs={'class': 'form-control'}),
        )

        self.fields['metodo'] = forms.ChoiceField(
            choices=[('Pix', 'Pix')],
            required=True,
            help_text='Ainda so aceitamos Pix :(',
        )       

        self.fields['valor'] = forms.DecimalField(
            required=True,
            max_digits=10,
            min_value=5
        )


#Form para validaçãos do form da aposta
class form_validação(forms.Form):
    escolha = forms.CharField(
    max_length=50,
    required=True,
    min_length=1,
    )

    metodo = forms.CharField(
    max_length=3,
    min_length=1,
    required=True,
    )

    valor = forms.DecimalField(
    max_digits=10,
    max_value=10000,
    min_value=10,
    required=True,
    error_messages={
        'max_digits': 'Só é permitido até 10 Digitos!',
        'max_value': 'Limite de 10 Mil por aposta!',
        'min_value': 'Apostas só acima de R$10,00!',
        'invalid': 'Este campo deve conter apenas números!'
    }
    )


        

        





