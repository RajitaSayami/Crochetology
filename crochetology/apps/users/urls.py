from django.urls import path
from . import views

urlpatterns = [
       path('users/profile', views.profile, name='profile'),
       path('users/password', views.password, name='password'),
       path('users/register', views.register, name='register')
       
]