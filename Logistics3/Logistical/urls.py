from django.urls import path
from Logistical import views


urlpatterns=[
    path('',views.orders,name='orders'),
    path('orders_form/',views.orders_form),
    path('orders_form/edit/<int:id>/',views.orders_form_edit),
    path('orders/', views.orders,name='orders'),
    path('orders_detail/<int:id>/', views.orders_detail,name='orders_orders_detail'),
    path('orders/orders_form/',views.orders_form),
    path('orders/orders_form/edit/<int:id>/',views.orders_form_edit,name='orders_edit'),
    path('orders/orders_form/',views.orders_form),
    path('orders/orders_delete/',views.orders_delete,name='orders_delete'),
    path('orders/orders_detail/<int:id>/', views.orders_detail, name='orders_detail'),
    path('orders/orders_detail/pdf/<int:id>/', views.generate_pdf, name='generate_orders_pdf'),
    path('suppliers/', views.suppliers,name='suppliers'),
    path('suppliers/suppliers_form/', views.suppliers_form),
    path('suppliers/suppliers_form/edit/<int:id>/', views.suppliers_form_edit,name='suppliers_edit'),
    path('suppliers/suppliers_delete/', views.suppliers_delete,name='suppliers_delete'),
    path('suppliers/suppliers_detail/<int:id>/', views.suppliers_detail,name='suppliers_detail'),
    path('pod/', views.pod,name='pod'),
    path('pod/pod_form/', views.pod_form,name='pod_form'),
    path('pod/pod_form/edit/<int:id>/', views.pod_form_edit,name='pod_edit'),
    path('pod/pod_delete/', views.pod_delete, name='pod_delete'),
    path('pod/pod_detail/<int:id>/', views.pod_detail, name='pod_detail'),
    path('taxes/', views.taxes,name='taxes'),
    path('taxes/tax_form/',views.tax_form,name='tax_form'),
    path('taxes/taxes_form/edit/<int:id>/',views.tax_form_edit,name='tax_edit'),
    path('taxes/tax_delete/',views.tax_delete,name='tax_delete'),
    path('taxes/taxes_detail/<int:id>/',views.taxes_detail,name='tax_detail'),
    path('products_and_services/', views.products_and_services,name='products'),
    path('products_and_services/products_form/',views.products_form),
    path('products_and_services/products_form/edit/<int:id>/',views.products_form_edit,name='products_edit'),
    path('products_and_services/products_delete/',views.products_delete,name='products_delete'),
    path('products_and_services/products_detail/<int:id>/', views.products_detail, name='products_detail'),
    path('customers/', views.customers,name='customers'),
    path('customers/customers_form/',views.customers_form),
    path('customers/customers_form/edit/<int:id>/',views.customer_form_edit,name='customers_edit'),
    path('customers/customers_delete/', views.customers_delete,name='customers_delete'),
    path('customers/customers_detail/<int:id>/', views.customers_detail,name='customers_detail'),
]