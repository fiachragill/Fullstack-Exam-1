from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Pizza

# forms
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'toppings', 'cheese']

class CustomerForm(forms.Form):
    # form fields
    name = forms.CharField(label='Name', max_length=100)
    card_number = forms.IntegerField(label='Card Number', min_value=10**15, max_value=10**16-1)
    expiry_date = forms.DateField(label='Expiry Date', input_formats=['%Y-%m'], widget=forms.TextInput(attrs={'type': 'month'}))
    cvv_number = forms.IntegerField(label='CVV Number', min_value=100, max_value=999)

    # custom validation
    def clean_expiry_date(self):
        card_expiry_date = self.cleaned_data['expiry_date']
        if card_expiry_date < datetime.now().date():
            raise ValidationError("Expiry date can not be in the past.")
        return card_expiry_date
