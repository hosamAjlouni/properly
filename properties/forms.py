from .models import Property, Unit
from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'year_built', 'description']
        
        labels = {
            'description': 'Desctiption',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Property Name',
                'autofocus'     : 'autofocus',
            }),
            
            'year_built': forms.DateInput(attrs={
                'type'          : 'date',
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Year Built',
            }),
            
            'description': forms.Textarea(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Desctiption',
            })
            
        }
        
        
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['property', 'num', 'beds', 'baths', 'size', 'market_rent', 'deposit', 'description']
        
        labels = {
            'description': 'Desctiption',
        }
        
        widgets = {
            'property': forms.Select(attrs={
                'autofocus'     : 'autofocus',
                'class'         : 'form-control shadow-sm',
            }),
            
            'num': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Unit Number',
            }),
            
            'beds': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : '# Beds',
            }),
            
            'baths': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : '# Baths',
            }),
            
            'size': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Size (sq.m.)',
            }),
            
            'market_rent': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Market Rent $',
            }),
            
            'deposit': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'deposit $',
            }),
            
            
            'description': forms.Textarea(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Desctiption',
            }),
            
        }