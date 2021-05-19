from django.db import models
from apps.users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

from apps.product.models import Product

class Order(models.Model):
    STATUS = [
        ('Complete', 'Complete'),
        ('Shipped', 'Shipped'),
        ('Pending', 'Pending'),
    ]
    PAID = [('Paid', 'Paid'), ('Unpaid', 'Unpaid'),]
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    email = models.EmailField(('email address'))
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    phone = PhoneNumberField(region="GB")
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    paid_status = models.CharField(max_length=10, choices = PAID, default='Unpaid')
    status = models.CharField(max_length=10, choices = STATUS, default='Pending')

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.email

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.product