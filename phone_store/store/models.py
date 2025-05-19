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
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.quantity * self.phone.price

    class Meta:
        unique_together = ('user', 'phone')  # Ngăn duplicate items

    def __str__(self):
        return f"{self.user.username} - {self.phone.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"