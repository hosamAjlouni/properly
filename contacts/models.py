from django.db import models
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
# Create your models here.


class Contact(models.Model):
    class Meta:
        ordering = ['first']
        unique_together = (('first', 'middle', 'last'),)
    
    first   = models.CharField(max_length=50, null=False, blank=False)
    middle  = models.CharField(max_length=50, null=False, blank=False)
    last    = models.CharField(max_length=50, null=False, blank=False)
    phone   = PhoneNumberField(blank=False, null=False, unique=True)
    user    = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='contacts')
    
    def balance(self):
        invoices = self.invoices.aggregate(invoices=Sum('amount'))['invoices']
        payments = self.payments.aggregate(payments=Sum('amount'))['payments']
        if not invoices:
            invoices = 0
        if not payments:
            payments = 0
            
        return invoices - payments
    
    def __str__(self):
        return f"{self.first.capitalize()} {self.last.capitalize()}"