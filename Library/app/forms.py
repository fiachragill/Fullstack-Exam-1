from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'toppings', 'cheese']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('email', 'card_number', 'ccv')