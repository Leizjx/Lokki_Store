from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Brand, Phone, Cart, Order, OrderItem
from django.utils import timezone

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = True
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_phone_number')
    list_select_related = ('profile',)

    def get_phone_number(self, instance):
        return instance.profile.phone_number if hasattr(instance, 'profile') else ''
    get_phone_number.short_description = 'Phone Number'

# Unregister the default UserAdmin and register our CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register other models
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    search_fields = ('user__username', 'phone_number')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'available')
    list_filter = ('brand', 'available')
    search_fields = ('name', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'quantity', 'total_price']
    list_filter = ['user']
    search_fields = ['user__username', 'phone__name']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Số lượng form trống để thêm mới
    fields = ('product', 'quantity', 'price')
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Nếu đang sửa đơn hàng
            return ('product', 'quantity', 'price')
        return []

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'total', 'get_status_display', 'get_payment_method', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('full_name', 'phone', 'id', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Thông tin khách hàng', {
            'fields': ('user', 'full_name', 'phone', 'address')
        }),
        ('Thông tin đơn hàng', {
            'fields': ('total', 'payment_method', 'status', 'order_note')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    inlines = [OrderItemInline]

    def get_status_display(self, obj):
        status_colors = {
            'pending': '<span style="color: #FF8C00;">⏳ Đang chờ xử lý</span>',
            'processing': '<span style="color: #0066CC;">⚙️ Đang xử lý</span>',
            'shipped': '<span style="color: #9932CC;">🚚 Đang giao hàng</span>',
            'completed': '<span style="color: #008000;">✅ Đã giao hàng</span>',
            'cancelled': '<span style="color: #FF0000;">❌ Đã hủy</span>'
        }
        return mark_safe(status_colors.get(obj.status, obj.status))
    get_status_display.short_description = 'Trạng thái'

    def get_payment_method(self, obj):
        payment_icons = {
            'cod': '💵 Thanh toán khi nhận hàng',
            'qr': '📱 Thanh toán QR',
            'bank': '🏦 Chuyển khoản ngân hàng'
        }
        return payment_icons.get(obj.payment_method, obj.payment_method)
    get_payment_method.short_description = 'Phương thức thanh toán'

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.readonly_fields + ('status', 'user', 'full_name', 'phone', 'address', 'payment_method', 'total')
        if obj: # Nếu đang sửa đơn hàng
            return self.readonly_fields + ('user', 'full_name', 'phone', 'address', 'payment_method', 'total')
        return self.readonly_fields

    def has_add_permission(self, request):
        return True  # Cho phép thêm đơn hàng

    def has_change_permission(self, request, obj=None):
        return True  # Cho phép sửa đơn hàng

    def save_model(self, request, obj, form, change):
        if not change:  # Nếu đang tạo mới
            obj.user = request.user
        obj.updated_at = timezone.now()
        super().save_model(request, obj, form, change)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'get_total']
    list_filter = ['order__status']
    search_fields = ['order__id', 'order__full_name', 'product__name']
    readonly_fields = ['order', 'product', 'quantity', 'price']

    def get_total(self, obj):
        return obj.quantity * obj.price
    get_total.short_description = 'Tổng tiền'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False