from django.forms import ModelForm
from .models import Taxes,Products_and_Services,Customers,Orders,Suppliers,Pod
from  django import forms

class TaxesForm(ModelForm):
    class Meta:
        model=Taxes
        fields={"tax_name","abbrevation","tax_rate"}

class ProductsForm(ModelForm):
    class Meta:
        model=Products_and_Services;
        fields='__all__'


class CustomersForm(ModelForm):
    class Meta:
        model=Customers;
        fields='__all__'

class SuppliersForm(ModelForm):
    class Meta:
        model=Suppliers;
        fields='__all__'




class OrdersForm(ModelForm):
    customer=forms.ModelChoiceField(queryset=Customers.objects.all(),required=True)
    name_supplier= forms.ModelChoiceField(queryset=Suppliers.objects.all(),required=True)
    sac= forms.ModelChoiceField(queryset=Products_and_Services.objects.all(),required=True)
    taxes=forms.ModelChoiceField(queryset=Taxes.objects.all(),required=True)

    class Meta:
        model=Orders;

        fields='__all__'

class PodForm(ModelForm):
    class Meta:
        model=Pod
        fields='__all__'




