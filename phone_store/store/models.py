from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Added back
    logo = models.ImageField(upload_to='brands/', blank=True)  # Added back
    
    def __str__(self):
        return self.name

class Phone(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='phones/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)  # Added back

    @property
    def total_price(self):
        return self.quantity * self.phone.price

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Đang chờ xử lý'),
        ('processing', 'Đang xử lý'),
        ('shipped', 'Đang giao hàng'),
        ('completed', 'Đã giao hàng'),
        ('cancelled', 'Đã hủy')
    )
    PAYMENT_CHOICES = (
        ('cod', 'Thanh toán khi nhận hàng'),
        ('qr', 'Thanh toán QR')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_note = models.TextField(blank=True)  # Added back
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Added back

    def __str__(self):
        return f'Order {self.id}'

class Profile(models.Model):  # Added back
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'