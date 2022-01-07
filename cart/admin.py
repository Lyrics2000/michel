from django.contrib import admin
from .models import Cart,CartQuantity,CartCustomer,CartQuantityCustomer
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'user','updates','timestamp']
    class Meta:
        model = Cart
admin.site.register(Cart,CartAdmin)
admin.site.register(CartQuantity)
admin.site.register(CartCustomer)
admin.site.register(CartQuantityCustomer)

