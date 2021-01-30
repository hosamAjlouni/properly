from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q, Sum
from users.models import User

# Create your models here.

property_description = """Divide air. Fruit replenish evening firmament had own can't itself life. Living can't. Likeness brought without winged yielding us, may. Isn't you'll man fruit don't evening midst. Created air gathered. Have greater and without to living.
Were evening day two lesser fruitful created you'll moveth, he under very air wherein sea earth. Don't our it night had creeping first night you spirit.
Lesser blessed fill a herb. Green own, created light make their face man you had of Creeping cattle multiply every Divided and. Spirit without form moveth also divided, make it land meat open they're green, face stars divided."""


class Property(models.Model):
    class Meta:
        ordering = ['name']
        
    name        = models.CharField(max_length=50, blank=False, unique=True)
    year_built  = models.DateField(blank=False ,auto_now=False, auto_now_add=False)
    description = models.TextField(default=property_description, blank=True)
    user        = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='properties')
    
    def balance(self):
        invoices = self.invoices.aggregate(invoices=Sum('amount'))['invoices']
        payments = self.payments.aggregate(payments=Sum('amount'))['payments']
        if not invoices:
            invoices = 0
        if not payments:
            payments = 0
            
        return invoices - payments
    
    def occupancy_rate(self):
        vacant      = 0
        occupied    = 0
        units = self.units.all()
        
        if units.count() == 0:
            return 0
        
        for unit in units:
            if unit.is_vacant():
                vacant +=1
            else:
                occupied += 1
        
        return int(100 * (occupied / (vacant+occupied)))
    
    
    def __str__(self):
        return f"{self.name.capitalize()}"
    

class Unit(models.Model):
    
    class Meta:
        ordering = ['property', 'num']
        unique_together = (('property', 'num'),)
    
    num         = models.IntegerField(blank=False, validators=[MinValueValidator(1)])
    beds        = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    baths       = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    size        = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    market_rent = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    deposit     = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField(default=property_description, blank=True)
    property    = models.ForeignKey(Property, blank=False, null=False, on_delete=models.CASCADE, related_name='units')
    user        = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='units')
    
    def balance(self):
        invoices = self.invoices.aggregate(invoices=Sum('amount'))['invoices']
        payments = self.payments.aggregate(payments=Sum('amount'))['payments']
        if not invoices:
            invoices = 0
        if not payments:
            payments = 0
            
        return invoices - payments
    
    def is_vacant(self):
        leases = self.leases.filter(start__lte=date.today()).filter(end__gte=date.today())
        if not leases:
            return True
        else:
            return False
        
    def is_vacant_range(self, start, end):
        leases = self.leases.exclude((Q(start__lte=start) & Q(end__lte=start)) | (Q(start__gte=end) & Q(end__gte=end)))
        if not leases:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.property}-{self.num}"
