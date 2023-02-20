from django import forms
from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'toppings', 'cheese']
