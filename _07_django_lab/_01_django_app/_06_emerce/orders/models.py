from django.db import models
from accounts.models import Account
from product.models import Product, Variation


# Create your models here.
class Payment(models.Model):
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id =  models.CharField(max_length=100)
    payment_method =  models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.payment_id

class Order(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Acceptd'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    )

    user =  models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address_lane_1 = models.CharField(max_length=100)
    address_lane_2 = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=120, blank=True)
    order_total = models.DecimalField(max_digits=15, decimal_places=2)
    tax = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def full_name(self):
        return f'{self.first_name}  {self.last_name}'

    
    def full_address(self):
        return f'{self.address_lane_1}  {self.address_lane_2}'

    def __str__(self):
        return self.email
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username