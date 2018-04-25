from django.urls import path
from Logistical import views


urlpatterns=[
    path('orders/', views.orders),
    path('customers/', views.customers),
    path('suppliers/', views.suppliers),
    path('products_and_services/', views.products_and_services),
    path('taxes/', views.taxes),
    path('pod/', views.pod),
    path('tax_form/',views.tax_form),
    path('products_form/',views.products_form),
    path('customers_form/',views.customers_form),
    path('suppliers_form/',views.suppliers_form),
    path('orders_form/',views.orders_form),
]