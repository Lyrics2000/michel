from django.shortcuts import render,redirect
# from billing.models import BillingProfile
# from accounts.forms import GuestForm
# from accounts.models import GuestEmail
# from address.forms import AddressForm,DeliveryTimeAddress
# from address.models import Address,DeliveryTime
# from oders.models import Order
from products.models import ProductQuantity, Products,Category,ProductDiscount
from .models import Cart, CartCustomer, CartQuantity, CartQuantityCustomer
from vendors.models import ResellProduct
# from oders.models import Order
# from decimal import Decimal
# from address.utils import API_KEY,gmap_key,distancePriceCalculator,newport_ri
# from geopy.geocoders import Nominatim
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
import math
from django.forms.models import model_to_dict


# {% url 'mpesa:cash_on_delivery' %}
# {% url 'mpesa:mpesaindex' %}


def get_percentage(dicount_percentage,original_price):
    percentage_discount = dicount_percentage
    calc = (percentage_discount * original_price)/100
    mn =  original_price - calc
    dicti = {}
    dicti['new_price'] = mn
    dicti['original_price'] = original_price
    dicti['percentage'] = percentage_discount
    return dicti


def cart_update(request):
    if request.is_ajax and request.method == "POST":
        print(request.POST)
        cart_id = request.session.get("cart_id")
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        print(product_id)


        products = [{
            "id": int(product_id),
            "product_qty" : int(quantity)
        }]
        obj,created = Cart.objects.get_or_create(id =  cart_id)
        for i in products:
            product_id = i['id']
            product_qty = i['product_qty']
            product_obj =  Products.objects.get(id = product_id)
            obj.products.add(product_obj)
            obj.save()
            carj,cret = CartQuantity.objects.get_or_create(cart = obj,product = product_obj )
            total_pri = float(product_qty) * float(product_obj.product_price)
            carj.quantity = float(product_qty)
            carj.total = total_pri
            carj.save()

        request.session['cart_items'] = obj.products.count()
        request.session['cart_id'] =  obj.id
        return redirect('vendors:vendor_shop_index')



    return redirect("carts:checkout")


def cart_remove(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        product_obj = Products.objects.get(id=product_id)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            # del  request.session['cart_id']
            
        
        request.session['cart_items'] = cart_obj.products.count()

    return redirect("/")

# Create your views here.

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:cart_home")  
    guest_form = GuestForm()
    shipping_address_id = request.session.get("delivery_address_id" , None)
    delivery_time_id  = request.session.get('delivery_time' , None)
    billing_profile, billing_profile_created  = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj,order_obj_created = Order.objects.new_or_get(billing_profile,cart_obj)
        if shipping_address_id:
            order_obj.delivery_address = Address.objects.get(id=shipping_address_id)
            #calculating shipping address
            shipping_addresses = Address.objects.get(id=shipping_address_id)
            print(shipping_addresses.address_line1)
            geolocator = Nominatim(user_agent="carts")
            # TODO: enable comments later for ditsance calculation
            # location = gmap_key.geocode(shipping_addresses.address_line1)
            # lat = location[0]["geometry"]["location"]["lat"]
            # lon = location[0]["geometry"]["location"]["lng"]
            # print("location" ,  location)
            # #customer location
            # cleveland_oh = (lat, lon)
            
            # #calculate the distace price
            # distancec  = geodesic(newport_ri, cleveland_oh).km
            # price = distancePriceCalculator(distance=distancec)
            #set shipping price to delivery price calculated
            # TODO : change order_obj.shipping_total = price once  google api key in address has been fixed
            order_obj.shipping_total = 200
            #TODO : replace math.fsum([cart_obj.total, 200] to math.fsum([cart_obj.total, price])
            new_total = math.fsum([cart_obj.total, 200])
            formatted_total = format(new_total,'2')
            order_obj.total = new_total


            if delivery_time_id:
                order_obj.delivery_time = DeliveryTime.objects.get(id=delivery_time_id)
        if  shipping_address_id:
            order_obj.save()
           
    cart_items  = cart_obj.products.count()
    allcategory = Category.objects.all()
    allbanners = Banners.objects.all()
    cartqty = CartQuantity.objects.all()
    google_api = API_KEY
   
    
    request.session['object'] = str(order_obj)
    request.session['cart'] = str(cart_obj)
    request.session['cart_items'] = cart_items
 
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
         "address_qs" : address_qs,
        "guest_form": guest_form,
        "cart_items" :  cart_items,
        "cart_obj" : cart_obj,
        "cart" : cart_obj,
        'categories' : allcategory,
        'allbanners'    : allbanners,
        'cartqty'    : cartqty,
        'google_api' : google_api
    }
    return render(request, "carts/checkout.html", context)


def cart_home(request):


    cart_obj,new_obj = Cart.objects.new_or_get(request)
    cart_items = cart_obj.products.count()
    allcategory = Category.objects.all()
    
    context = {
        'cart' : cart_obj,
        'cart_items' : cart_items,
        'categories' : allcategory,
    } 
    return redirect("/")



def cart_update_customer(request):
    if request.is_ajax and request.method == "POST":
        print(request.POST)
        cart_id = request.session.get("cart_id")
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        print(product_id)


        products = [{
            "id": int(product_id),
            "product_qty" : int(quantity)
        }]
        obj,created = CartCustomer.objects.get_or_create(id =  cart_id)
        for i in products:
            product_id = i['id']
            product_qty = i['product_qty']
            product_obj =  ResellProduct.objects.get(id = product_id)
            obj.products.add(product_obj)
            obj.save()
            carj,cret = CartQuantityCustomer.objects.get_or_create(cart = obj,product = product_obj )
            total_pri = float(product_qty) * float(product_obj.product_price)
            carj.quantity = float(product_qty)
            carj.total = total_pri
            carj.save()

        request.session['cart_items'] = obj.products.count()
        request.session['cart_id'] =  obj.id
        return redirect('/')



    return redirect("carts:checkout")

