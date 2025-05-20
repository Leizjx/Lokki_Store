from django.contrib import admin
from .models import Phone, Brand, Cart, Order, OrderItem

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'stock', 'available']
    list_filter = ['available', 'brand']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock', 'available']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'quantity', 'total_price']
    list_filter = ['user']
    search_fields = ['user__username', 'phone__name']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'total', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['full_name', 'phone', 'address']
    readonly_fields = ['user', 'full_name', 'phone', 'address', 'payment_method', 'total', 'created_at']
    inlines = [OrderItemInline]
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    search_fields = ['order__full_name', 'product__name']
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False