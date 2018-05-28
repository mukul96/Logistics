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

        def __init__(self, *args, **kwargs):
            super(CustomersForm, self).__init__(*args, **kwargs)
            self.fields['gstin'].required = False
            self.fields['email'].required = False
            self.fields['website'].required = False
            self.fields['postal_code'].required = False
            self.fields['address1'].required = False
            self.fields['address2'].required = False
            self.fields['remark'].required = False


class SuppliersForm(ModelForm):
    class Meta:
        model=Suppliers;
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(SuppliersForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['pan_number'].required = False
        self.fields['no_own_vehicles'].required = False
        self.fields['alternate_number'].required = False


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
        def __init__(self, *args, **kwargs):
            super(PodForm, self).__init__(*args, **kwargs)
            self.fields['receiver_name'].required = False
            self.fields['receiver_account_number'].required = False
            self.fields['bank_name'].required = False
            self.fields['payment_date'].required = False
            self.fields['amount'].required = False






