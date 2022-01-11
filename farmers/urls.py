
from django.urls import path
from .views import (
    index,
    all_categories,
    add_category,
    all_products,
    add_product,
    product_view,
    edit_category,
    edit_cat,
    delete_category,
    farmer_products

)


app_name = "farmers"
urlpatterns = [
    path('',index,name="index"),
    path('all_categories/',all_categories,name="all_categories"),
    path('add_category/',add_category,name="add_category"),
    path('all_products/',all_products,name="all_products"),
    path('add_product/',add_product,name="add_product"),
    path('product_view/<id>/',product_view,name="product_view"),
    path('edit_cat/<id>/',edit_category,name="edit_category"),
    path('edit_category/',edit_cat,name="edit_cat"),
    path("delete_product/<id>/",delete_category,name="delete_category"),
    path("farmer_orders/",farmer_products,name="farmer_products")
]