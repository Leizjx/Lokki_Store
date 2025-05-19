from django.db import models
from django.contrib.auth.models import User
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', blank=True)

    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='phones/')
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.brand.name} {self.name}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.phone.price * self.quantity