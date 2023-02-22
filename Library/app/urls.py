from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', create_pizza, name='all_pizza'),
    path('customer/<int:pizza_id>/', customer_details, name='customer_details'),
]