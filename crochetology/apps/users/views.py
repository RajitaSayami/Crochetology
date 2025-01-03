from django.shortcuts import render

# Create your views here.


def password(request):
    return render(request, 'users/password.html')

def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')
