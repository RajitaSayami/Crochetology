from django.shortcuts import render

def products(request):
    return render(request, 'products.html')  # Create a corresponding template

def bouquet(request):
    return render(request, 'bouquet.html')

def winter(request):
    return render(request, 'winter.html')

def keyring(request):
    return render(request, 'keyring.html')

def hair(request):
    return render(request, 'hair.html')

def accessories(request):
    return render(request, 'accessories.html')

def bag(request):
    return render(request, 'bag.html')

def contact(request):
    return render(request, 'footer.html')  # Contact page


