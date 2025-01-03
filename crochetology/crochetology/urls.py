"""
URL configuration for crochetology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# In crochectology/urls.py
from django.contrib import admin
from django.urls import path, include
from crochetology import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('apps.products.urls')),
    path('users/', include('apps.users.urls')),
    path('orders/', include('apps.orders.urls')),
    path('', views.home, name='home'),  # Add this line to handle the root URL
    path('', views.faq, name='faq'),
    path('about/', views.faq, name='faq'),
    path('products/', views.products, name='products'),# Main products pag
    path('bag/', views.products_bag, name='product-bag'),
    path('bouquet/', views.products_bouquet, name='product-bouquet'),  # Bouquet category
    path('winter/', views.products_winter, name='product-winter'),  # Winter essentials
    path('keyring/', views.products_keyring, name='product-keyring'),  # Key rings
    path('hair/', views.products_hair, name='product-hair'),  # Hair accessories
    path('accessories/', views.products_accessories, name='product-accessories'),  # Accessories
    path('orders/details/', views.orders_details, name='details'),
    path('orders/customization/', views.orders_customization, name='customization'),  # Customization page
    path('orders/cart/', views.orders_cart,name='cart'),
    path('users/login', views.users_login, name='login'),
    path('users/password', views.users_password, name='password'),
    path('users/register', views.users_register, name='register'),
]
    