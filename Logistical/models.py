from django.db import models
import datetime
# Create your models here.

class Customers(models.Model):
    first_name=models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email=models.EmailField()
    phone_number=models.IntegerField()
    website=models.URLField()
    state=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    postal_code=models.IntegerField()
    address_1=models.TextField()
    address_2=models.TextField()

    def __str__(self):
        return u'{0}'.format(self.first_name)

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
    def __str__(self):
        return u'{0}'.format(self.supplier_name)

class Products_and_Services(models.Model):
    description=models.TextField()
    sac=models.IntegerField()
    Taxes=models.IntegerField()
    def __str__(self):
        return u'{0}'.format(self.sac)

class Taxes(models.Model):
    tax_name=models.TextField()
    abbrevation=models.TextField()
    tax_rate=models.IntegerField()
    def __str__(self):
        return u'{0}'.format(self.tax_name)

class Orders(models.Model):
    description = models.TextField()
    invoice_date=models.DateField(default=datetime.datetime.now())
    payment_due=models.DateField(default=datetime.datetime.now())
    service_origin=models.CharField(max_length=512)
    service_destination=models.CharField(max_length=512)
    truck_number=models.CharField(max_length=512)
    truck_type=models.CharField(max_length=512)
    driver_name=models.CharField(max_length=256)
    driver_number=models.IntegerField()
    advance_money=models.IntegerField(default=0)
    balance_money=models.IntegerField()
    mobile_number=models.IntegerField()
    service_fee = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    total = models.IntegerField()
    total_in_words = models.TextField()
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name_supplier= models.ForeignKey(Suppliers, related_name="name_supplier", on_delete=models.CASCADE)
    sac = models.ForeignKey(Products_and_Services, related_name="saca", on_delete=models.CASCADE)
    taxes = models.ForeignKey(Taxes, on_delete=models.CASCADE)



























