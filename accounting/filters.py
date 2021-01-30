import django_filters
from .models import Invoice

class InvoiceFilter(django_filters.FilterSet):
    class Meta:
        model   = Invoice
        fields  = ['amount', 'category', 'due_date', 'property', 'unit', 'contact', ]