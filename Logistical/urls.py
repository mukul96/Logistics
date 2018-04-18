from django.urls import path
from Logistical import views


urlpatterns=[
    path('orders/', views.orders),
    path('customers/', views.customers),
    path('suppliers/', views.suppliers),
    path('products_and_services/', views.products_and_services),
    path('taxes/', views.taxes),
    path('pod/', views.pod),
]