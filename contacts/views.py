from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def all(request):
    contacts = Contact.objects.all()
    
    return render(request, 'contacts/all.html', {
        'title'     : 'All Contacts',
        'contacts'  : contacts,
    })
    

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def add(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(False)
            contact.user = request.user
            contact.save()
            return redirect(reverse('contacts:all'))
        
        else:
            return render(request, 'contacts/form.html', {
                'form_title' : 'Add Contact',
                'form'  : form,
            })
            
    form = ContactForm()
    return render(request, 'contacts/form.html', {
        'form_title' : 'Add Contact',
        'form'  : form,
    })
    
    
@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, "contacts/contact.html", {
        "contact" : contact
    })