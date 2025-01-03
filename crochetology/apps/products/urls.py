from django.urls import path
from . import views

urlpatterns = [
    
    path('products/', views.products, name='products'),# Main products pag
    path('bag', views.bag, name='bag'),
    path('bouquet/', views.bouquet, name='bouquet'),  # Bouquet category
    path('winter/', views.winter, name='winter'),  # Winter essentials
    path('keyring/', views.keyring, name='keyring'),  # Key rings
    path('hair/', views.hair, name='hair'),  # Hair accessories
    path('accessories/', views.accessories, name='accessories'),  # Accessories
    path('contact/', views.contact, name='footer'),
    
 
    
  
    
]
