from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('phones/', views.phone_list, name='phone_list'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:phone_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('brands/', views.brand_list, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('search/', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]