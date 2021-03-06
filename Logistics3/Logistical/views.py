from django.shortcuts import render,HttpResponse,redirect
from .models import Customers,Products_and_Services,Suppliers,Taxes,Orders
from .forms import *
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.conf import settings
import weasyprint
from weasyprint import HTML
import tempfile
# Create your views here.
@login_required(login_url='/login')
def orders(request):
    order=Orders.objects.all()
    return (render(request, "orders.html", {'order':order}))

@login_required(login_url='/login')
def customers(request):
    customer=Customers.objects.all()

    return (render(request,"customers.html",{'customer':customer}))

@login_required(login_url='/login')
def suppliers(request):
    supplier=Suppliers.objects.all()
    return (render(request,"suppliers.html",{'supplier':supplier}))

@login_required(login_url='/login')
def products_and_services(request):
    products=Products_and_Services.objects.all()
    return (render(request,"products_and_services.html",{'products':products}))

@login_required(login_url='/login')
def taxes(request):
    tax=Taxes.objects.all()
    return (render(request,"taxes.html",{'tax':tax}))

@login_required(login_url='/login')
def pod(request):
    pod=Pod.objects.all()
    return (render(request,"pod.html",{'pod':pod}))

@login_required(login_url='/login')
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
               return redirect(reverse('taxes'))
       else:
           form = TaxesForm
           context_data = {'form': form}
           return render(request,'taxes_form.html', context_data)

@login_required(login_url='/login')
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
            return redirect(reverse('products'))
    else:
        form = ProductsForm
        context_data = {'form': form}
        return render(request, 'products_form.html', context_data)

@login_required(login_url='/login')
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
            return redirect(reverse('suppliers'))
    else:
        form = SuppliersForm
        context_data = {'form': form}
        return render(request, 'suppliers_form.html', context_data)

@login_required(login_url='/login')
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
            return redirect(reverse('customers'))
    else:
        form = CustomersForm
        context_data = {'form': form}
        return render(request, 'customers_form.html', context_data)

@login_required(login_url='/login')
def orders_form(request):
    if request.method == 'POST':

        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('orders'))
        return redirect(reverse('orders'))
    else:
        form=OrdersForm
        context_data = {'form': form}
        return render(request, 'orders_form.html', context_data)

@login_required(login_url='/login')
def pod_form(request):
    if request.method == 'POST':

        form = PodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pod'))
        return redirect(reverse('pod'))
    else:
        form=PodForm
        context_data = {'form': form}
        return render(request, 'pod_form.html', context_data)

@login_required(login_url='/login')
def tax_form_edit(request,id):
    #print("checking")

    instance = get_object_or_404(Taxes, id=id)
    print(instance)
    form = TaxesForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('taxes'))
    return render(request, 'taxes_form.html', {'form': form})

@login_required(login_url='/login')
def customer_form_edit(request,id):
    #print("checking")
    if id:
        instance = get_object_or_404(Customers, id=id)
        print(instance)
        form = CustomersForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('customers'))
        return render(request, 'customers_form.html', {'form': form})

@login_required(login_url='/login')
def products_form_edit(request,id):
    #print("checking")
    if id:
        instance = get_object_or_404(Products_and_Services, id=id)
        print(instance)
        form = ProductsForm(request.POST or None, instance=instance)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
        return render(request, 'products_form.html', {'form': form})

@login_required(login_url='/login')
def suppliers_form_edit(request,id):
    print("checking")

    instance = get_object_or_404(Suppliers, id=id)
    print(instance)
    form = SuppliersForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('suppliers'))
    return render(request, 'suppliers_form.html', {'form': form})

@login_required(login_url='/login')
def orders_form_edit(request,id):
    #print("checking")

    instance = get_object_or_404(Orders, id=id)
    print(instance)
    form = OrdersForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('orders'))
    return render(request, 'orders_form.html', {'form': form})

@login_required(login_url='/login')
def pod_form_edit(request,id):
    #print("checking")

    instance = get_object_or_404(Pod, id=id)
    print(instance)
    form = PodForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('pod'))
    return render(request, 'pod_form.html', {'form': form})

@login_required(login_url='/login')
def tax_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Taxes, id=id)
    instance.delete()
    return redirect(reverse('taxes'))

@login_required(login_url='/login')
def suppliers_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Suppliers, id=id)
    instance.delete()
    return redirect(reverse('suppliers'))

@login_required(login_url='/login')
def products_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Products_and_Services, id=id)
    instance.delete()
    return redirect(reverse('products'))

@login_required(login_url='/login')
def customers_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Customers, id=id)
    instance.delete()
    return redirect(reverse('customers'))

@login_required(login_url='/login')
def orders_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Orders, id=id)
    instance.delete()
    return redirect(reverse('orders'))

@login_required(login_url='/login')
def pod_delete(request):
    id=request.POST['id']
    instance = get_object_or_404(Pod, id=id)
    instance.delete()
    return redirect(reverse('pod'))


@login_required(login_url='/login')
def taxes_detail(request,id):
    tax=Taxes.objects.get(id=id);
    return render(request,"taxes_detail.html",{'tax':tax})

@login_required(login_url='/login')
def taxes_detail(request,id):
    tax=Taxes.objects.get(id=id);
    return render(request,"taxes_detail.html",{'tax':tax})

@login_required(login_url='/login')
def orders_detail(request,id):
    order=Orders.objects.get(id=id);
    return render(request,"orders_detail.html",{'order':order})

@login_required(login_url='/login')
def customers_detail(request,id):
    Customer=Customers.objects.get(id=id);
    list_of_orders=[]
    orders=Orders.objects.all()
    for o in orders:
        if o.customer==Customer:
            list_of_orders.append(o)
    return render(request,"customers_detail.html",{'customer':Customer,'orders':list_of_orders})

@login_required(login_url='/login')
def pod_detail(request,id):
    pod=Pod.objects.get(id=id);
    return render(request,"pod_detail.html",{'pod':pod})

@login_required(login_url='/login')
def suppliers_detail(request,id):
    supplier=Suppliers.objects.get(id=id);
    return render(request,"suppliers_detail.html",{'supplier':supplier})

@login_required(login_url='/login')
def products_detail(request,id):
    product=Products_and_Services.objects.get(id=id);
    return render(request,"products_detail.html",{'product':product})



@login_required(login_url='/login')
def generate_pdf(request,id):
    """Generate pdf."""
    # Model data
    order = Orders.objects.get(id=id)

    # Rendered
    html_string = render_to_string('pdf.html', {'order': order})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
