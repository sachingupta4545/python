from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255,  null=true)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"
    
class Collection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='collections')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='collections')
    