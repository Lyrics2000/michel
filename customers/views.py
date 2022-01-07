from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from cart.models import Cart, CartQuantity
from cart.models import CartCustomer,CartQuantityCustomer
from django.contrib import messages
from django.db.models import Sum
from products.models import (
    Category,
    ProductQuerySet,
    Products
)

from vendors.models import ResellProduct

# Create your views here.
def index(request):
    all_products =  ResellProduct.objects.all()
    print(all_products)
    all_categories = Category.objects.all()
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    if cart_id:
        cart_obj =  CartCustomer.objects.get(id = cart_id if cart_id is not None  else 0)
        cart_quantyty_obj  =  CartQuantityCustomer.objects.filter(cart = cart_obj)
        featured_products = ResellProduct.objects.filter(featured_product = True)
        total_cart = CartQuantityCustomer.objects.filter(cart = cart_obj).aggregate(Sum('total'))

        context = {
            'products':all_products,
            'all_categoris':all_categories,
            'featured_products' : featured_products,
            'cart_items' : cart_items,
            'cart_quantity' : cart_quantyty_obj,
            'total': total_cart['total__sum']
        }
        return render(request,'./customer_shop/customer_shop_index.html',context)

    else:
       
        featured_products = ResellProduct.objects.filter(featured_product = True)
        context = {
            'products':all_products,
            'all_categoris':all_categories,
            'featured_products' : featured_products,
            'cart_items' : cart_items,
            
        }
        return render(request,'./customer_shop/customer_shop_index.html',context)




def product_detailed(request,id):
    cart_items = request.session.get("cart_items")
    single_product = ResellProduct.objects.get(id =  id)
    all_categories = Category.objects.all()
    user_obj = User.objects.get(id =  single_product.user.id)
    more_like_this = ResellProduct.objects.filter(user = user_obj)
    featured_products = ResellProduct.objects.filter(featured_product = True)
    context = {
        'single_product':single_product,
        'more_like_this': more_like_this,
        'featured_products':featured_products,
        'all_categoris':all_categories,
         'cart_items' : cart_items
    }
    return render(request,'./customer_shop/shop_detailed.html',context)






@login_required(login_url='account:sign_in')
def checkout(request):
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    cart_obj =  CartCustomer.objects.get(id = int(cart_id))
    cart_quantyty_obj  =  CartQuantityCustomer.objects.filter(cart = cart_obj)
    total_cart = CartQuantityCustomer.objects.filter(cart = cart_obj).aggregate(Sum('total'))
    all_categories = Category.objects.all()

    context = {
        'total': total_cart['total__sum'],
        'cart_items' : cart_items,
        'cart_quantity' : cart_quantyty_obj,
        'all_categoris':all_categories,


    }

    return render(request,'./customer_shop/checkout.html',context)



@login_required(login_url='account:sign_in')
def order_placed(request):
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    cart_obj =  CartCustomer.objects.get(id = int(cart_id) if cart_id is not None  else 0)
    cart_quantyty_obj  =  CartQuantityCustomer.objects.filter(cart = cart_obj)
    total_cart = CartQuantityCustomer.objects.filter(cart = cart_obj).aggregate(Sum('total'))
    all_categories = Category.objects.all()
    del request.session['cart_items']
    del request.session['cart_id']
    del request.session['checkout_id']
    del request.session['merchant_id']
    del request.session['phone_no']

    context = {
        'total': total_cart['total__sum'],
        'cart_items' : cart_items,
        'cart_quantity' : cart_quantyty_obj,
        'all_categoris':all_categories,


    }
    return render(request,'./customer_shop/order_placed.html',context)

