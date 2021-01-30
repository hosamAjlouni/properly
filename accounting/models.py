from django.db import models
from django.db.models import Sum
from users.models import User
from leases.models import Lease
from contacts.models import Contact
from properties.models import Unit, Property
from django.core.validators import MinValueValidator
from datetime import date

# Create your models here.

invoice_categories = (('Rent Amount', 'Rent Amount'),
                      ('Security Deposit', 'Security Deposit'),
                      ('Water Fee','Water Fee'),
                      ('Electricity Fee', 'Electricity Fee'),
                      ('Service Fee', 'Service Fee')
                      )

class Invoice(models.Model):
    
    class Meta:
        ordering = ['-due_date']
    
    amount      = models.DecimalField(blank=False, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category    = models.CharField(max_length=50, blank=False, null=False, choices=invoice_categories, default='Rent Amount')
    due_date    = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    property    = models.ForeignKey(Property, blank=False, null=False, on_delete=models.CASCADE, related_name='invoices')
    unit        = models.ForeignKey(Unit, blank=False, null=False, on_delete=models.CASCADE, related_name='invoices')
    contact     = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE, related_name='invoices')
    lease       = models.ForeignKey(Lease, blank=False, null=False, on_delete=models.CASCADE, related_name='invoices')
    user        = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='invoices')
    
    def __str__(self):
        return f"{self.contact} - {self.amount}$"
    
    def amount_paid(self):
        amount_paid = self.payments.aggregate(amount_paid=Sum('amount'))['amount_paid']
        
        if amount_paid:
            return float(amount_paid)
        else:
            return float(0)
    
    def balance(self):
        return float(self.amount) - float(self.amount_paid())
    
    def is_paid(self):
        if self.amount == self.amount_paid():
            return True
        else:
            return False

    def status(self):
        if self.is_paid():
            return 'Paid'
        elif self.amount_paid() and self.balance():
            return 'Partial'
        elif self.balance() and self.due_date <= date.today():
            return 'Overdue'
        else:
            return 'Open'

class Payment(models.Model):
    amount      = models.DecimalField(blank=False, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    date        = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    invoice     = models.ForeignKey(Invoice, blank=False, null=False, on_delete=models.CASCADE, related_name='payments')
    property    = models.ForeignKey(Property, blank=False, null=False, on_delete=models.CASCADE, related_name='payments')
    unit        = models.ForeignKey(Unit, blank=False, null=False, on_delete=models.CASCADE, related_name='payments')
    contact     = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE, related_name='payments')
    user        = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='payments')