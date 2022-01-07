from django.urls import path 
from .views import (
    cart_home,
    checkout_home,
    cart_update,
    cart_remove,
    cart_update_customer
)


app_name = 'cart'

urlpatterns = [
    path('',cart_home,name= 'cart_home'),
     path('checkout',checkout_home,name= 'checkout'),
     path('update',cart_update,name= 'cart_update'),
     path('remove',cart_remove,name= 'cart_remove_product'),
     path("cart_update_customer/",cart_update_customer,name="cart_update_customer")
]

