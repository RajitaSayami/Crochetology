from django.shortcuts import render

# Create your views here.


def password(request):
    return render(request, 'users/password.html')

def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    return render(request, 'users/register.html')
