from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')