from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

class Customer(models.Model):

    MEMBERSHIP_BASIC = 'BASIC'
    MEMBERSHIP_PREMIUM = 'PREMIUM'
    MEMBERSHIP_VIP = 'VIP'

    # Define choices for membership types
    MEMBERSHIP_CHOICES = [
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    membership = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BASIC)

class Order(models.Model):

    ORDER_PENDING = 'Pending'
    ORDER_SHIPPED = 'Shipped'
    ORDER_DELIVERED = 'Delivered'
    ORDER_CANCELLED = 'Cancelled'

    # Define choices for order status
    ORDER_STATUS_CHOICES = [
        (ORDER_PENDING, 'Pending'),
        (ORDER_SHIPPED, 'Shipped'),
        (ORDER_DELIVERED, 'Delivered'),
        (ORDER_CANCELLED, 'Cancelled'),
    ]

    # Define the Order model with a foreign key to Customer and Product
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default=ORDER_PENDING)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'product')  # Ensure a product can only appear once in an order
