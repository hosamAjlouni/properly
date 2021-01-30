from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model   = Contact
        fields  = ['first', 'middle', 'last', 'phone']
        
        labels = {
            'first': 'First Name',
            'Last': 'Last Name',
        }
        
        widgets = {
            'first': forms.TextInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'First Name',
                'autofocus'     : 'autofocus',
            }),
            
            'middle': forms.TextInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Middle Name (Optional)',
            }),
            
            'last': forms.TextInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Last Name',
                'autofocus'     : 'autofocus',
            }),
            
            'phone': forms.TextInput(attrs={
                'class'         : 'form-control shadow-sm',
                'placeholder'   : 'Phone Number',
            })
        }