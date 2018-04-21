from django.contrib import admin
from .models import Orders,Products_and_Services,Suppliers,Taxes,Customers
# Register your models here.

admin.site.register(Orders);
admin.site.register((Suppliers));
admin.site.register(Taxes);
admin.site.register(Customers)
admin.site.register(Products_and_Services)


