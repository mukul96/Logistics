from django.db import models
import datetime
# Create your models here.
STATUS_CHOICES = (
    (1, (2.5)),
    (2, (6)),
    (3, (8.5)),
    (4, (14))
)

class Customers(models.Model):
    company_name=models.CharField(max_length=256)
    gstin=models.CharField(max_length=256)
    customer_type=models.CharField(max_length=256)
    first_name=models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.IntegerField()
    state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    email=models.EmailField(blank=True,null=True)
    website=models.URLField(blank=True,null=True)
    postal_code=models.IntegerField(blank=True,null=True)
    address_1=models.TextField(blank=True,null=True)
    address_2=models.TextField(blank=True,null=True)
    remark=models.TextField(blank=True,null=True)
    def __str__(self):
        return u'{0}'.format(self.first_name)

class Suppliers(models.Model):
    company_name=models.CharField(max_length=256)
    supplier_name=models.CharField(max_length=256)
    type_of_supplier=models.CharField(max_length=512,default='manufacturer')
    mobile_number = models.IntegerField()
    service_origin1 = models.CharField(max_length=256)
    service_origin2 = models.CharField(max_length=256)
    service_origin3 = models.CharField(max_length=256)
    service_origin4 = models.CharField(max_length=256)
    service_origin5 = models.CharField(max_length=256)
    service_destination1 = models.CharField(max_length=256)
    service_destination2 = models.CharField(max_length=256)
    service_destination3 = models.CharField(max_length=256)
    service_destination4 = models.CharField(max_length=256)
    service_destination5 = models.CharField(max_length=256)
    pan_number=models.CharField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    no_own_vehicles=models.IntegerField(default=1,blank=True,null=True)
    alternate_number=models.IntegerField(default=mobile_number,blank=True,null=True)
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
    sgst=models.IntegerField(choices=STATUS_CHOICES,default=1)
    cgst=models.IntegerField(choices=STATUS_CHOICES,default=1)


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




























