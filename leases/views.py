from django.shortcuts import render, redirect, reverse
from .models import Lease
from properties.models import Unit
from datetime import date
from .forms import LeaseForm
from accounting.forms import LeaseInvoiceForm
from .filters import LeaseFilter
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def all(request):
    leases      = Lease.objects.all()
    leaseFilter = LeaseFilter(request.GET, queryset=leases)
    qs          = leaseFilter.qs
                
    return render(request, 'leases/leases.html', {
        'title'         : 'Leases',
        'leaseFilter'   : leaseFilter,
        'qs'            : qs,
    })


@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def active(request):
    leases = Lease.objects.all()
    
    return render(request, 'leases/active.html', {
        'title' : 'Active Leases',
        'leases': leases
    })


@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector'])
def add(request, unit_id=None):

    if request.method == 'POST':
        form        = LeaseForm(data=request.POST)
        invoiceForm = LeaseInvoiceForm(data=request.POST)

        if form.is_valid() and invoiceForm.is_valid():
            lease               = form.save(False)
            lease.user          = request.user
            lease.property      = lease.unit.property
            lease.save()
            
            invoice             = invoiceForm.save(False)
            invoice.property    = lease.property
            invoice.unit        = lease.unit
            invoice.contact     = lease.tenant
            invoice.lease       = lease
            invoice.user        = request.user
            invoice.save()
            
            redirect(reverse('leases:all'))
                    
        else:
            return render(request, 'leases/form.html', {
                'form'          : form,
                'form_title'    : 'Add Lease',
                'invoice_form'  : invoiceForm
            })
        
    if unit_id:
        form = LeaseForm(initial={'unit':Unit.objects.get(id=unit_id)})
    else:
        form = LeaseForm()
    
    invoiceForm = LeaseInvoiceForm()
    
    return render(request, 'leases/form.html', {
        'form'          : form,
        'form_title'    : 'Add Lease',
        'invoice_form'  : invoiceForm
    })