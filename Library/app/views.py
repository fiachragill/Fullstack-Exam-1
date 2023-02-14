from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            return render(request, 'details.html', {'pizza': pizza})
        else:
            render(request, 'create_pizza.html', {'form': form})
    else:
        form = PizzaForm()
        return render(request, 'create_pizza.html', {'form': form})
