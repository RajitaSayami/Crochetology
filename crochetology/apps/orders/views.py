from django.shortcuts import render

# Create your views here.
def customization(request):
    return render(request, 'orders/customization.html')
def cart(request):
    return render(request, 'orders/cart.html')
def details(request):
    return render(request, 'orders/detail.html')