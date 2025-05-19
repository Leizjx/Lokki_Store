from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  # Thêm dòng này
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Phone, Brand, Cart
from django.core.paginator import Paginator

def home(request):
    brands = Brand.objects.all()
    phones_list = Phone.objects.order_by('-id').all()
    
    # Phân trang, mỗi trang 8 sản phẩm
    paginator = Paginator(phones_list, 12)
    page = request.GET.get('page')
    featured_phones = paginator.get_page(page)
    
    return render(request, 'store/home.html', {
        'brands': brands,
        'featured_phones': featured_phones
    })

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'store/phone_list.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    return render(request, 'store/phone_detail.html', {'phone': phone})

@login_required
def add_to_cart(request, phone_id):
    if request.method == 'POST':  # Chỉ xử lý request POST
        phone = get_object_or_404(Phone, id=phone_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            phone=phone,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        messages.success(request, f"{phone.name} đã được thêm vào giỏ hàng!")
        return redirect('cart')
    return redirect('phone_detail', phone_id=phone_id)

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Sản phẩm đã được xóa khỏi giỏ hàng!")
    return redirect('cart')

def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Phone.objects.filter(name__icontains=query)
    return render(request, 'store/search.html', {
        'query': query,
        'results': results
    })

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'store/brands.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    phones = brand.phone_set.all()
    return render(request, 'store/brand_detail.html', {
        'brand': brand,
        'phones': phones
})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        # Update user information
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
        
    return render(request, 'store/profile.html')

@login_required
def update_cart_quantity(request, cart_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Cart.objects.get(id=cart_id)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')

@login_required
def cart_summary(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.phone.price * item.quantity for item in cart_items)
    return render(request, 'store/cart_summary.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.phone.price * item.quantity for item in cart_items)
    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required 
def checkout_confirm(request):
    if request.method == 'POST':
        # Xử lý thanh toán ở đây
        cart_items = Cart.objects.filter(user=request.user)
        cart_items.delete()  # Xóa giỏ hàng sau khi thanh toán
        return redirect('checkout_success')
    return redirect('checkout')