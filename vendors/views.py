from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from cart.models import Cart, CartQuantity
from django.contrib import messages
from django.db.models import Sum
from payment.models import PaidCustomer
from products.models import (
    Category,
    ProductQuerySet,
    Products
)
from .models import (
    ResellProduct
)

# Create your views here.
@login_required(login_url='account:sign_in') 
def index(request):

    user_obj =  User.objects.get(id =  request.user.id)
    paid_c =  PaidCustomer.objects.filter().count()
    product_c = ResellProduct.objects.filter(user =  user_obj).count()
    processing = PaidCustomer.objects.filter(processed =  True)
    system_c = Products.objects.all().count()
    all_orders = PaidCustomer.objects.filter(paid = True)



    context = {
        "paid_c": paid_c,
        "product_c" : product_c  ,
        "processing" : processing,
        "system_c" : system_c,
        "all_orders":all_orders
    }
    
    return render(request,'vendor_index.html',context)


@login_required(login_url='account:sign_in') 
def vendors_products(request):
    all_orders = PaidCustomer.objects.filter(paid = True)

    context = {
         "all_orders":all_orders

    }
    return render(request,'orders_vendor.html',context)

@login_required(login_url='account:sign_in') 
def shop_index(request):
    all_products =  Products.objects.all()
    all_categories = Category.objects.all()
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    if cart_id:
        cart_obj =  Cart.objects.get(id = cart_id if cart_id is not None  else 0)
        cart_quantyty_obj  =  CartQuantity.objects.filter(cart = cart_obj)
        featured_products = Products.objects.filter(featured_product = True)
        total_cart = CartQuantity.objects.filter(cart = cart_obj).aggregate(Sum('total'))

        context = {
            'products':all_products,
            'all_categoris':all_categories,
            'featured_products' : featured_products,
            'cart_items' : cart_items,
            'cart_quantity' : cart_quantyty_obj,
            'total': total_cart['total__sum']
        }
        return render(request,'./shop/shop_index.html',context)

    else:
       
        featured_products = Products.objects.filter(featured_product = True)
        context = {
            'products':all_products,
            'all_categoris':all_categories,
            'featured_products' : featured_products,
            'cart_items' : cart_items,
            
        }
        return render(request,'./shop/shop_index.html',context)




@login_required(login_url='account:sign_in')
def product_detailed(request,id):
    cart_items = request.session.get("cart_items")
    single_product = Products.objects.get(id =  id)
    all_categories = Category.objects.all()
    user_obj = User.objects.get(id =  single_product.user.id)
    more_like_this = Products.objects.filter(user = user_obj)
    featured_products = Products.objects.filter(featured_product = True)
    context = {
        'single_product':single_product,
        'more_like_this': more_like_this,
        'featured_products':featured_products,
        'all_categoris':all_categories,
         'cart_items' : cart_items
    }
    return render(request,'./shop/shop_detailed.html',context)



@login_required(login_url='account:sign_in')
def all_products(request):
    cart_items = request.session.get("cart_items")
    all_categories = Category.objects.all()
    all_products = Products.objects.all()
    name = "All Products"

    context = {
        'all_categoris':all_categories,
        'all_products':all_products,
        'name':name,
        'cart_items' : cart_items
    }
    return render(request,'./shop/all_products.html',context)


@login_required(login_url='account:sign_in')
def checkout(request):
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    cart_obj =  Cart.objects.get(id = int(cart_id))
    cart_quantyty_obj  =  CartQuantity.objects.filter(cart = cart_obj)
    total_cart = CartQuantity.objects.filter(cart = cart_obj).aggregate(Sum('total'))
    all_categories = Category.objects.all()

    context = {
        'total': total_cart['total__sum'],
        'cart_items' : cart_items,
        'cart_quantity' : cart_quantyty_obj,
        'all_categoris':all_categories,


    }

    return render(request,'./shop/checkout.html',context)



@login_required(login_url='account:sign_in')
def order_placed(request):
    cart_items = request.session.get("cart_items")
    cart_id =  request.session.get("cart_id")
    cart_obj =  Cart.objects.get(id = int(cart_id) if cart_id is not None  else 0)
    cart_quantyty_obj  =  CartQuantity.objects.filter(cart = cart_obj)
    total_cart = CartQuantity.objects.filter(cart = cart_obj).aggregate(Sum('total'))
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
    return render(request,'./shop/order_placed.html',context)



@login_required(login_url='account:sign_in')
def featured_products(request):
    cart_items = request.session.get("cart_items")
    all_categories = Category.objects.all()
    all_products = Products.objects.filter(featured_product =  True)
    name = "Featured Products"

    context = {
        'all_categoris':all_categories,
        'all_products':all_products,
        'name':name,
        'cart_items' : cart_items
    }
    return render(request,'./shop/all_products.html',context)



@login_required(login_url='account:sign_in')
def category_detailed_product(request,id):
    one_cat =  Category.objects.get(id =  int(id))
    cart_items = request.session.get("cart_items")
    all_categories = Category.objects.all()
    all_products = Products.objects.filter(product_category =  one_cat)
    name = f"Category : {one_cat.category_name}"

    context = {
        'all_categoris':all_categories,
        'all_products':all_products,
        'name':name,
        'cart_items' : cart_items
    }
    return render(request,'./shop/all_products.html',context)



@login_required(login_url='account:sign_in') 
def all_products(request):
  
    cart_items = request.session.get("cart_items")
    all_categories = Category.objects.all()
    all_products = Products.objects.all()
    name = "All Products"

    context = {
        'all_categoris':all_categories,
        'all_products':all_products,
        'name':name,
        'cart_items' : cart_items
    }
    return render(request,'./shop/all_products.html',context)


@login_required(login_url='account:sign_in')
def product_view(request,id):
    product = Products.objects.get(id = id)
    context = {
        'product':product
    }
    return render(request,'vendor_product_view.html',context)

@login_required(login_url='account:sign_in')
def add_product(request,id):
    product = Products.objects.get(id =  id)
    context = {
        "product":product
    }
    return render(request,'vendor_add_product.html',context)


@login_required(login_url='account:sign_in')
def resell_product(request):
    user_id =  request.user.id
    user_obj =  User.objects.get(id =  user_id)
    if request.method == "POST":
        prod_id =  request.POST.get("product_id")
        product_obj =  Products.objects.get(id = int(prod_id))
        product_price =  request.POST.get("product_price")
        status =  request.POST.get("status")
        image =  request.FILES['image']
        featured = request.POST.get("featured")
       
        ResellProduct.objects.create(
            user = user_obj,
            product = product_obj,
            product_price = product_price,
            product_image = image,
            Active =  True if status == 'Active' else False,
            featured_product = True if featured == "Yes" else False
        )
        messages.success(request, 'Product saved successfully.')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        print(request.POST)
    
    return render(request,'vendor_add_product.html')



@login_required(login_url='account:sign_in') 
def resell_all_products(request):
    
    user_obj =  User.objects.get(id =  request.user.id)
    all_products =  ResellProduct.objects.filter(user =  user_obj)
    context = {
        'all_products':all_products
    }
    return render(request,'vendor_resell_all_products.html',context)





