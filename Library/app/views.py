# import statements
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Customer, Order
from .forms import PizzaForm, CustomerForm

# views
def index(request):
    return render(request, 'index.html')

def create_pizza(request):
    if request.method == "POST":
        new_pizza_form = PizzaForm(request.POST)
        if new_pizza_form.is_valid():
            new_pizza = new_pizza_form.save()
            return redirect('customer_details', pizza_id=new_pizza.id)
    else:
        new_pizza_form = PizzaForm()
    
    return render(request, 'create_pizza.html', {'form': new_pizza_form})

def customer_details(request, pizza_id):
    # get the pizza object with the given id
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    
    if request.method == "POST":
        # create a form for the customer details and validate it
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            # get or create a customer object with the given name
            name = customer_form.cleaned_data['name']
            customer, created = Customer.objects.get_or_create(name=name)
            
            # create an order object for the customer and pizza
            order = Order(paid=True, customer=customer, pizza=pizza)
            order.save()
            
            return render(request, 'success_page.html', {'order': order})
    else:
        customer_form = CustomerForm()
    
    return render(request, 'details.html', {'form': customer_form, 'pizza': pizza})
