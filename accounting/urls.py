from django.urls import path
from . import views

app_name = 'accounting'

urlpatterns = [
    path('add', views.add_invoice, name='add_invoice'),
    path('invoices', views.invoices, name='invoices'),
    path('payment/<int:invoice_id>/', views.rec_payment, name='rec_payment')
]