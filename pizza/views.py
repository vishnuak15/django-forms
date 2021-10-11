from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request,'pizza/home.html')

def order(request):
    forms = PizzaForm()
    return render(request,'pizza/order.html',{'Pizzaform':forms})