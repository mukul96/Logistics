from django.urls import path
from Logistical import views


urlpatterns=[
    path('orders/', views.orders,name='orders'),
    path('orders/orders_form/',views.orders_form),
    path('orders/orders_form/edit/<int:id>/',views.orders_form_edit),
    path('orders/orders_delete/',views.orders_delete,name='orders_delete'),
    path('suppliers/', views.suppliers,name='suppliers'),
    path('suppliers/suppliers_form/', views.suppliers_form),
    path('suppliers/suppliers_form/edit/<int:id>/', views.suppliers_form_edit),
    path('suppliers/suppliers_delete/', views.suppliers_delete,name='suppliers_delete'),
    path('pod/', views.pod),
    path('taxes/', views.taxes,name='taxes'),
    path('taxes/tax_form/',views.tax_form,name='tax_form'),
    path('taxes/tax_form/edit/<int:id>/',views.tax_form_edit),
    path('taxes/tax_delete/',views.tax_delete,name='tax_delete'),
    path('products_and_services/', views.products_and_services,name='products'),
    path('products_and_services/products_form/',views.products_form),
    path('products_and_services/products_form/edit/<int:id>/',views.products_form_edit),
    path('products_and_services/products_delete/',views.products_delete,name='products_delete'),
    path('customers/', views.customers,name='customers'),
    path('customers/customers_form/',views.customers_form),
    path('customers/customers_form/edit/<int:id>/',views.customer_form_edit),
    path('customers/customers_delete/', views.customers_delete,name='customers_delete'),
]