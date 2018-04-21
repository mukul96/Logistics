from django.shortcuts import render,HttpResponse,redirect
from .models import Customers,Products_and_Services,Suppliers,Taxes

# Create your views here.
def orders(request):
    return (render(request,"order.html",{}))

def customers(request):
    return (render(request,"customers.html",{}))

def suppliers(request):
    return (render(request,"suppliers.html",{}))

def products_and_services(request):
    return (render(request,"products_and_services.html",{}))

def taxes(request):
    return (render(request,"taxes.html",{}))

def pod(request):
    return (render(request,"pod.html",{}))

