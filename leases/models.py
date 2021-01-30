from django.db import models
from users.models import User
from properties.models import Unit, Property
from contacts.models import Contact
from datetime import date

# Create your models here.

class Lease(models.Model):
    class Meta:
        ordering = ['-start', 'end', 'property', 'unit']
        
    property    = models.ForeignKey(Property, blank=False, null=False, on_delete=models.CASCADE, related_name='leases')
    unit        = models.ForeignKey(Unit, blank=False, null=False, on_delete=models.CASCADE, related_name='leases')
    tenant      = models.ForeignKey(Contact, blank=False, null=False, on_delete=models.CASCADE, related_name='leases')
    start       = models.DateField(blank=False, null=False, auto_now=False, auto_now_add=False)
    end         = models.DateField(blank=False, null=False, auto_now=False, auto_now_add=False)
    ended       = models.BooleanField(default=False)
    user        = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='leases')

    def is_past(self):
        if self.end < date.today():
            return True
        else:
            return False
        
    def is_active(self):
        if self.start <= date.today() <= self.end:
            return True
        else:
            return False
        
    def is_future(self):
        if self.start > date.today():
            return True
        else:
            return False
    
    def status(self):
        if self.is_past():
            return 'past'
        if self.is_active():
            return 'active'
        if self.is_future():
            return 'future'
    
    def __str__(self):
        return f'{self.unit} / {self.tenant} - Lease#({self.id})'