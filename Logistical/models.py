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
    type_of_supplier=models.CharField(max_length=512,default='manufacturer')
    mobile_number = models.IntegerField()
    service_origin = models.TextField()
    service_destination = models.TextField()
    pan_number=models.IntegerField(blank=True)
    address=models.TextField(blank=True)
    no_own_vehicles=models.IntegerField(default=1,blank=True)
    alternate_number=models.IntegerField(default=mobile_number,blank=True)
    def __str__(self):
        return u'{0}'.format(self.supplier_name)

class Products_and_Services(models.Model):
    description=models.TextField(null=False,blank=False)
    sac=models.IntegerField(null=False,blank=False)
    Taxes=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return u'{0}'.format(self.sac)

class Taxes(models.Model):
    tax_name=models.TextField(null=False,blank=False)
    abbrevation=models.TextField(null=False,blank=False)
    tax_rate=models.IntegerField(null=False,blank=False)
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
    freight=models.IntegerField(default=0)


class Pod(models.Model):
    pod_receiving_date=models.DateField(default=datetime.datetime.now())
    loading_date=models.DateField(default=datetime.datetime.now())
    lr_number=models.IntegerField()
    truck_number=models.CharField(max_length=512)
    receiver_name=models.CharField(max_length=512)
    receiver_account_number=models.CharField(max_length=512)
    bank_name=models.CharField(max_length=512)
    amount=models.IntegerField()
    payment_date=models.DateField(default=datetime.datetime.now())
    remarks=models.TextField(null=True,blank=True)
    consignor_name=models.CharField(max_length=512)




























