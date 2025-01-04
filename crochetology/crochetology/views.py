# In your views.py (could be in the 'crochetology' app or another app like 'home')
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def users_login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def home(request):
    return render(request, 'project.html')

def products(request):
    return render(request, 'project.html')  # Create a corresponding template

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

def users_login(request):
    return render(request, 'users/login.html')


def users_register(request):
    return render(request, 'users/register.html')


def faq(request):
    return render(request, 'faq.html')
