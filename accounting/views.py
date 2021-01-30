from django.shortcuts import render, redirect, reverse
from .models import Invoice, Payment
from .forms import LeaseInvoiceForm, PaymentForm
from .filters import InvoiceFilter
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from datetime import date

# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def add_invoice(request):
    form = LeaseInvoiceForm()
    
    return render(request, 'accounting/invoiceForm.html', {
        'form'          : form,
        'form_title'    : 'Add Invoice'
    })

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def invoices(request):
    invoices        = Invoice.objects.all()
    invoiceFilter   = InvoiceFilter(request.GET, queryset=invoices)
    invoices        = invoiceFilter.qs
    
    return render(request, 'accounting/invoices.html', {
        'title'     : 'Inovices',
        'invoices'  : invoices,
        'filter'    : invoiceFilter
    })
    
@login_required
@allowed_users(allowed_roles=['admin', 'collector', 'accountant'])
def rec_payment(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    
    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            payment = form.save(False)
            payment.date = date.today()
            payment.property = invoice.property
            payment.unit = invoice.unit
            payment.contact = invoice.contact
            payment.user = request.user
            payment.save()
            return redirect(reverse('accounting:invoices'))            
            
        else:
            return redirect(reverse('home:index'))
    
    else:
        form = PaymentForm(initial={'invoice': invoice})
        
        return render(request, 'accounting/paymentForm.html', {
            'form'          : form,
            'form_title'    : 'Record Payment',
            'invoice'       : invoice
        })