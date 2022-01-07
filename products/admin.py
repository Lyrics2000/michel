from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (Category,Products,ProductDiscount,ProductQuantity,
ProductImage)

# Register your models here.
# class MoreProductQuantityInline(admin.StackedInline):
#         model = MoreProductQuantirty
# class PostImageAdmin(admin.StackedInline):
#         model = PostImage

admin.site.register(ProductImage)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug']
    class Meta:
        model = Category
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'slug' , 'product_category','product_price',
'featured_product']
#     inlines = [MoreProductQuantityInline,PostImageAdmin]
    class Meta:
        model = Products

class ProductQuantityAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'final_quantity' , 'created_at']
    class Meta:
        model = ProductQuantity

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(ProductQuantity,ProductQuantityAdmin)
admin.site.register(ProductDiscount)
