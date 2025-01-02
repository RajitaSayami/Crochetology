# In your views.py (could be in the 'crochetology' app or another app like 'home')
from django.shortcuts import render

def products(request):
    return render(request, 'products.html')  # Create a corresponding template

def products_bouquet(request):
    return render(request, 'products/bouquet.html')

def products_winter(request):
    return render(request, 'products/winter.html')

def products_keyring(request):
    return render(request, 'products/keyring.html')

def products_hair(request):
    return render(request, 'products/hair.html')

def products_accessories(request):
    return render(request, 'products/accessories.html')

def products_bag(request):
    return render(request, 'products/bag.html')

def contact(request):
    return render(request, 'footer.html')  # Contact page

def orders_details(request):
    return render(request, 'orders/details.html')

def orders_customization(request):
    return render(request, 'orders/customization.html')

def orders_cart(request):
    return render(request, 'orders/cart.html')

def users_password(request):
    return render(request, 'users/password.html')

def users_profile(request):
    return render(request, 'users/profile.html')


def users_register(request):
    return render(request, 'users/register.html')


def home(request):
    return render(request, 'base.html')

def faq(request):
    return render(request, 'faq.html')
