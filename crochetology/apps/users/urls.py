from django.urls import path
from . import views

urlpatterns = [
       path('profile/', views.profile, name='profile'),
       path('password/', views.password, name='password'),
       path('register/', views.register, name='register')
       
]