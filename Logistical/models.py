from django.db import models

# Create your models here.

class Customers(models.Model):
    first_name=models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email=models.EmailField()
    phone_number=models.IntegerField()
    website=models.URLField()
    state=models.CharField()
    city=models.CharField()
    postal_code=models.IntegerField()
    address_1=models.TextField()
    address_2=models.TextField()

class Suppliers(models.Model):
    company_name=models.CharField(max_length=256)
    supplier_name=models.CharField(max_length=256)
    pan_number=models.IntegerField()
    mobile_number=models.IntegerField()
    address=models.TextField()
    no_own_vehicles=models.IntegerField(default=1)
    alternate_number=models.IntegerField(default=mobile_number)
    service_origin=models.TextField()
    service_destination=models.TextField()

class Products_and_Services(models.Model):
    description=models.TextField()
    sac=models.IntegerField()
    Taxes=models.IntegerField()

class Orders(models.Model):
    name=models.CharField(max_length=256)
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    invoice_date=models.DateField()
    payment_due=models.DateField()
    service_origin=models.CharField()
    service_destination=models.CharField()
    truck_number=models.TextField()
    truck_type=models.TextField()
    driver_name=models.CharField()
    driver_number=models.IntegerField()
    advance_money=models.IntegerField()
    balance_money=models.IntegerField()
    mobile_number=models.IntegerField()
    supplier_name=models.ForeignKey(Suppliers,default=Suppliers.supplier_name)
    number_supplier=models.ForeignKey(Suppliers,default=Suppliers.mobile_number)
    pan_number=models.ForeignKey(Suppliers,default=Suppliers.pan_number)
    sac=models.ForeignKey(Products_and_Services,default=Products_and_Services.sac)
    description=models.TextField()
    service_fee=models.IntegerField()
    taxes=models.IntegerField()
    discount=models.IntegerField()
    total=models.IntegerField()
    total_in_words=models.TextField()









class Taxes(models.Model):
    tax_name=models.TextField()
    abbrevation=models.TextField()
    tax_rate=models.IntegerField()









