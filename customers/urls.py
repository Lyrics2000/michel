
from django.urls import path
from .views import (
    index,
    product_detailed,
    checkout,
    order_placed

)
app_name = "customers"
urlpatterns = [
    path('',index,name="index"),
    path("product_detailed/<id>",product_detailed,name="product_detailed"),
     path('checkout/',checkout,name="checkout"),
     path('order_placed_success/',order_placed,name="order_placed"),
    
]