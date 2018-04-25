from django.shortcuts import render,HttpResponse,redirect
from .models import Customers,Products_and_Services,Suppliers,Taxes,Orders
from .forms import *
# Create your views here.
def orders(request):
    return (render(request,"order.html",{}))

def customers(request):
    customer=Customers.objects.all()

    return (render(request,"customers.html",{'customer':customer}))

def suppliers(request):
    supplier=Suppliers.objects.all()
    return (render(request,"suppliers.html",{'supplier':supplier}))

def products_and_services(request):
    products=Products_and_Services.objects.all()
    return (render(request,"products_and_services.html",{'products':products}))

def taxes(request):
    tax=Taxes.objects.all()
    return (render(request,"taxes.html",{'tax':tax}))

def pod(request):
    return (render(request,"pod.html"))

def tax_form(request):
       if request.method == 'POST':
           form = TaxesForm(request.POST)
           if form.is_valid():
               # save the model to database, directly from the form:
               Taxes= form.save(commit=False)  # reference to my_model is often not needed at all, a simple form.save() is ok
               # alternatively
               # my_model = form.save(commit=False)  # create model, but don't save to database
               # my.model.something = whatever  # if I need to do something before saving it
               Taxes.save()
               return HttpResponse("taxes added")
       else:
           form = TaxesForm
           context_data = {'form': form}
           return render(request,'taxes_form.html', context_data)


def products_form(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            Products_and_Services = form.save(commit=False)  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            Products_and_Services.save()
            return HttpResponse("products_and_services added")
    else:
        form = ProductsForm
        context_data = {'form': form}
        return render(request, 'products_form.html', context_data)


def suppliers_form(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            Suppliers = form.save(commit=False)  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            Suppliers.save()
            return HttpResponse("Suppliers added")
    else:
        form = SuppliersForm
        context_data = {'form': form}
        return render(request, 'suppliers_form.html', context_data)


def customers_form(request):
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            Customers = form.save(commit=False)  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            Customers.save()
            return HttpResponse("Customers added")
    else:
        form = CustomersForm
        context_data = {'form': form}
        return render(request, 'customers_form.html', context_data)


def orders_form(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            # save the model to database, directly from the form:
            Orders = form.save(commit=False)  # reference to my_model is often not needed at all, a simple form.save() is ok
            # alternatively
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            Orders.save()
            return HttpResponse("Customers added")
    else:
        form = OrdersForm
        context_data = {'form': form}
        return render(request, 'orders_form.html', context_data)


