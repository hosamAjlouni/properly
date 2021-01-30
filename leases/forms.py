from .models import Lease
from django import forms
from properties.models import Unit

class LeaseForm(forms.ModelForm):
    class Meta:
        model   = Lease
        fields  = ['unit', 'tenant', 'start', 'end']
        
        widgets = {
            'unit': forms.Select(attrs={
                'class'         : 'form-control shadow-sm',
            }),
            
            'tenant': forms.Select(attrs={
                'class'         : 'form-control shadow-sm',
            }),
            
            'start': forms.DateInput(attrs={
                'type'          : 'date',
                'class'         : 'form-control shadow-sm',
            }),
            
            'end': forms.DateInput(attrs={
                'type'          : 'date',
                'class'         : 'form-control shadow-sm',
            }),
        }
        
    def clean(self):
        cleaned_data = super(LeaseForm, self).clean()
        unit    = cleaned_data.get('unit')
        start   = cleaned_data.get('start')
        end     = cleaned_data.get('end')
        errors  = []

        if not unit.is_vacant_range(start, end):
            errors.append('This Unit is not available for the given period')
        
        if start >= end:
            errors.append('StartDate should be earlier than EndDate')
            
        if errors:
            raise forms.ValidationError(errors)
        
        return cleaned_data
        