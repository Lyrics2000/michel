
from os import name
from django.urls import path
from .views import (
    index,
    shop_index,
    product_detailed,
    all_products,
    checkout,
    order_placed,
    featured_products,
    category_detailed_product,
    all_products,
    product_view,
    add_product,
    resell_product,
    resell_all_products

)
app_name = "vendors"
urlpatterns = [
    path("all_p/",all_products,name="all_products"),
    path('',index,name="index"),
    path('vendor/shop_index/',shop_index,name="vendor_shop_index"),
    path('product_detailed/<id>/',product_detailed,name="product_detailed"),
    path('all_products/',all_products,name="all_products"),
    path('vender/checkout/',checkout,name="checkout"),
    path('order_placed_success/',order_placed,name="order_placed"),
    path("featured_products/",featured_products,name="featured_products"),
    path("category_detailed_product/<id>/",category_detailed_product,name="category_detailed_product"),
    path("vendor_product_view/<id>/",product_view,name="product_view"),
    path("resell_product/<id>",add_product,name="add_product"),
    path("resell_products",resell_product,name="resell_product"),
    path("resell_all/",resell_all_products,name="resell_all_products")
    
]