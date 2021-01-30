from .models import Invoice, Payment
from django import forms


class LeaseInvoiceForm(forms.ModelForm):
    class Meta:
        model   = Invoice
        fields  = ['amount', 'category', 'due_date']
        
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class'         : 'form-control shadow-sm',
            }),
            
            'category': forms.Select(attrs={
                'type'          : 'date',
                'class'         : 'form-control shadow-sm',
            }),
            
            'due_date': forms.DateInput(attrs={
                'type'          : 'date',
                'class'         : 'form-control shadow-sm',
            }),
        }
        

class PaymentForm(forms.ModelForm):
    class Meta:
        model   = Payment
        fields  = ['amount', 'invoice']
        
        widgets = {
                'amount': forms.NumberInput(attrs={
                'class'     : 'form-control shadow-sm',
                }),
                
                'invoice': forms.TextInput(attrs={
                    # 'disabled'  : 'disabled',
                    'readonly'  : 'readonly',
                    'class'     : 'form-control shadow-sm',
                }),
            }