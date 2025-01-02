from django.urls import path
from . import views

urlpatterns = [
    path('orders/customization/', views.customization, name='customization'),  # Customization page
    path('orders/cart/', views.cart,name='cart'),
    path('orders/details', views.details, name='detail')
    
    
]