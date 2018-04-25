from django.forms import ModelForm
from .models import Taxes,Products_and_Services,Customers,Orders,Suppliers

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
    class Meta:
        model=Suppliers;
        fields='__all__'