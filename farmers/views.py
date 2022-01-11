from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from products.models import (Category, ProductDiscount,
Products
)
from django.contrib import messages
from payment.models import (
    Paid
)

# Create your views here.
@login_required(login_url='account:sign_in') 
def index(request):

    user_obj =  User.objects.get(id =  request.user.id)
    paid_c =  Paid.objects.filter().count()
    product_c = Products.objects.filter(user =  user_obj).count()
    processing = Paid.objects.filter(processed =  True)
    system_c = Products.objects.all().count()
    all_orders = Paid.objects.filter(paid = True)



    context = {
        "paid_c": paid_c,
        "product_c" : product_c  ,
        "processing" : processing,
        "system_c" : system_c,
        "all_orders":all_orders
    }
    
    return render(request,'farmer_index.html',context)


@login_required(login_url='account:sign_in') 
def farmer_products(request):
    all_orders = Paid.objects.filter(paid = True)

    context = {
         "all_orders":all_orders

    }
    return render(request,'orders_farmer.html',context)



@login_required(login_url='account:sign_in') 
def all_categories(request):
    user_id = request.user.id
    all_categories = Category.objects.filter(user_id = user_id)
    context = {
        'all_categories':all_categories
    }
    return render(request,'all_categories.html',context)


@login_required(login_url='account:sign_in') 
def add_category(request):
    if request.method == "POST":
        user_id = request.user.id
        category_name = request.POST.get("name")
        category_image = request.FILES['image']
        description = request.POST.get("description")
        status = request.POST.get("status")
        user_obj =  User.objects.get(id =  user_id)
        if status == "Active":        
            Category.objects.create(user = user_obj,
            category_name = category_name,
            category_image = category_image ,
            description = description,
            status = False
            )
            messages.success(request, 'Category saved successfully.')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            Category.objects.create(user = user_obj,
            category_name = category_name,
            category_image = category_image ,
            description = description,
            status = True
            )
            messages.success(request, 'Category saved successfully.')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        
    return render(request,'add_category.html')


@login_required(login_url='account:sign_in') 
def all_products(request):
    user_id = request.user.id
    all_products =  Products.objects.filter(user_id = user_id)
    context = {
        'all_products':all_products
    }
    return render(request,'all_products.html',context)


@login_required(login_url='account:sign_in')
def add_product(request):
    user_id =  request.user.id
    user_obj =  User.objects.get(id =  user_id)
    all_category =  Category.objects.filter(user_id =  user_id)
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        category_id =  request.POST.get("categtory")
        product_price =  request.POST.get("product_price")
        status =  request.POST.get("status")
        image =  request.FILES['image']
        featured = request.POST.get("featured")
        short_description =  request.POST.get("short_description")
        long_description =  request.POST.get("long_description")
        category_obj  = Category.objects.get(id = int(category_id))
        
        Products.objects.create(
            user = user_obj,
            product_title = product_name,
            product_overview = short_description,
            product_full_description = long_description,
            product_category = category_obj,
            product_price =  product_price,
            product_Image_Field = image,
            Active =  True if status == 'Active' else False,
            featured_product = True if featured == "Yes" else False
        )
        messages.success(request, 'Product saved successfully.')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))





        print(request.POST)
    context = {
        'all_categories' : all_category
    }
    return render(request,'add_product.html',context)


@login_required(login_url='account:sign_in')
def product_view(request,id):
    product = Products.objects.get(id = id)
    context = {
        'product':product
    }
    return render(request,'product_view.html',context)


@login_required(login_url='account:sign_in') 
def edit_category(request,id):
    one_cat = Category.objects.get(id = id)
    context = {
        'one_cat':one_cat
    }
   
    return render(request,'category_edit.html',context)


@login_required(login_url='account:sign_in') 
def delete_category(request,id):
    one_cat = Category.objects.delete()
    
   
    return redirect("farmers:all_categories")


@login_required(login_url='account:sign_in') 
def edit_cat(request):
     if request.method == "POST":
        id =  request.POST.get("id")
        print("idd",id)
        one_cat = Category.objects.get(id = id)
        user_id = request.user.id
        category_name = request.POST.get("name")
        category_image = request.FILES['image']
        description = request.POST.get("description")
        status = request.POST.get("status")
        user_obj =  User.objects.get(id =  user_id)
        one_cat.category_name = category_name
        one_cat.category_image = category_image
        description = description
        status =  True if status == "Active" else False
        messages.success(request, 'Category saved successfully.')
        return redirect("farmers:all_categories")
        

