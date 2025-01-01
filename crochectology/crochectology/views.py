# In your views.py (could be in the 'crochectology' app or another app like 'home')
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def faq(request):
    return render(request, 'faq.html')