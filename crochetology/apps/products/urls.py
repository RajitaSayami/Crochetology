from django.urls import path
from . import views

urlpatterns = [
    
    path('products/', views.products, name='products'),# Main products pag
    path('products/bag', views.bag, name='bag'),
    path('products/bouquet/', views.bouquet, name='bouquet'),  # Bouquet category
    path('products/winter/', views.winter, name='winter'),  # Winter essentials
    path('products/keyring/', views.keyring, name='keyring'),  # Key rings
    path('products/hair/', views.hair, name='hair'),  # Hair accessories
    path('products/accessories/', views.accessories, name='accessories'),  # Accessories
    path('contact/', views.contact, name='footer'),
    
 
    
  
    
]
