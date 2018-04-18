from django.db import models

# Create your models here.
class Orders(models.Model):
    name=models.CharField(max_length=256)

class Customers(models.Model):
    name=models.CharField(max_length=256)


class Suppliers(models.Model):
    name=models.CharField(max_length=256)

class Taxes(models.Model):
    name=models.CharField(max_length=256)

class Products_and_Services(models.Model):
    name=models.CharField(max_length=256)




