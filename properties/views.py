from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Property, Unit
from .forms import PropertyForm, UnitForm
from .filters import UnitFilter
from users.decorators import allowed_users

# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def all(request):
    properties = Property.objects.all()
    
    return render(request, 'properties/properties.html', {
        'properties': properties,
        'title': 'Properties',
    })
    

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def units(request):
    units       = Unit.objects.all()
    unitFilter  = UnitFilter(request.GET, queryset=units)
    qs          = unitFilter.qs
    message     = None
    
    if 'vacant_in_min' in request.GET and 'vacant_in_max' in request.GET:
        if request.GET['vacant_in_min'] != '' and request.GET['vacant_in_max'] != '':
            start   = request.GET['vacant_in_min']
            end     = request.GET['vacant_in_max']
            av_units = []
            
            for unit in unitFilter.qs:
                if unit.is_vacant_range(start, end):
                    av_units.append(unit)
                    
            qs = av_units
            
        elif request.GET['vacant_in_min'] != '' or request.GET['vacant_in_max'] != '':
            message = 'Provide Start and End dates please.'
            

    
    return render(request, 'properties/units.html', {
        'title'         : 'Units',
        'unitFilter'    : unitFilter,
        'qs'            : qs,
        'message'       : message
    })
    

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def property(request, property_id):
    property = Property.objects.get(id=property_id)
    
    return render(request, 'properties/property.html', {
        'title': 'Property',
        'property' : property,
    })


@login_required
@allowed_users(allowed_roles=['admin', 'accountant'])
def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        
        if form.is_valid():
            property = form.save(False)
            property.user = request.user
            property.name = property.name.lower()
            property.save()
            
            return redirect(reverse('properties:all'))
        
        else:            
            return render(request, 'properties/property_form.html', {
                'form_title': 'Add Property',
                'form' : form
            })
            
    
    return render(request, 'properties/property_form.html', {
        'form_title': 'Add Property',
        'form' : PropertyForm(),
    })


@login_required
@allowed_users(allowed_roles=['admin', 'accountant'])
def property_edit(request, property_id):
    
    property = Property.objects.get(id=property_id)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        
        if form.is_valid():
            property = form.save(False)
            property.user = request.user
            property.name = property.name.lower()
            property.save()
            
            return redirect(reverse('properties:all'))
        
        else:            
            return render(request, 'properties/property_form.html', {
                'form_title': 'Add Property',
                'form' : form
            })
            
    
    return render(request, 'properties/property_edit.html', {
        'property'        : property,
        'form_title': 'Edit  Property',
        'form'      : PropertyForm(instance=property),
    })    

@login_required
@allowed_users(allowed_roles=['admin', 'accountant'])
def unit_add(request, property_id=None):
    if request.method == 'POST':
        form = UnitForm(data=request.POST)

        if form.is_valid():
            unit = form.save(False)
            unit.user = request.user
            unit.save()
            return redirect(reverse('properties:property', kwargs={'property_id': unit.property.id}))
        
        else:
            return render(request, 'properties/unit_form.html', {
                'form_title': 'Add Unit',
                'form': form,
            })
    
    if property_id:
        form = UnitForm(initial={'property': Property.objects.get(id=property_id)})
    else:
        form = UnitForm()
    
    return render(request, 'properties/unit_form.html', {
        'form_title': 'Add Unit',
        'form': form,
    })

@login_required
@allowed_users(allowed_roles=['admin', 'sales', 'collector', 'accountant'])
def unit(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    return render(request, 'properties/unit.html', {
        'unit' : unit,
    })