from django.shortcuts import render, get_object_or_404
from .models import Phone, Brand
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Cart
from django.contrib.auth.forms import UserCreationForm

def home(request):
    brands = Brand.objects.all()
    featured_phones = Phone.objects.order_by('-id')[:4]
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
    phone = get_object_or_404(Phone, id=phone_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        phone=phone,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})