from django.shortcuts import render

def products(request):
    return render(request, 'products.html')  # Create a corresponding template

def bouquet(request):
    return render(request, 'products/bouquet.html')

def winter(request):
    return render(request, 'products/winter.html')

def keyring(request):
    return render(request, 'products/keyring.html')

def hair(request):
    return render(request, 'products/hair.html')

def accessories(request):
    return render(request, 'products/accessories.html')

def bag(request):
    return render(request, 'products/bag.html')

def contact(request):
    return render(request, 'footer.html')  # Contact page


