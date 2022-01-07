from django.db import models
from account.models import User
import random
import os
from django.db.models import Q, base
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from config.utils import unique_slug_generator,category_unique_slug_generator
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

def upload_image_path2(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "categories/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class Category(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    category_name = models.CharField(max_length=50)
    category_image = models.FileField(upload_to = upload_image_path2 ,null=True,blank=False)
    description =  models.TextField(blank=True,null=True)
    status =  models.BooleanField(default=False)
    slug = models.SlugField(blank=True,unique=True)
    

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse("farmers:edit_category", kwargs={
            'id': self.id
        })

    def delete_absolute_url(self):
        return reverse("farmers:delete_category", kwargs={
            'id': self.id
        })

    def vendor_category_detailed(self):
        
        return reverse("vendors:category_detailed_product", kwargs={
            'id': self.id
        })

    

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(Active=True)
    def featured(self):
        return self.filter(featured_product=True)
    def search(self, query):
        lookups = (Q(product_title__icontains=query) | 
                  Q(product_full_description__icontains=query) |
                  Q(product_price__icontains=query) 
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def all(self):
        return self.get_queryset().active()
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def featured(self): #Product.objects.featured() 
        return self.get_queryset().featured()
    def search(self, query):
        return self.get_queryset().active().search(query)





class Products(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product_title = models.CharField(max_length=100)
    product_overview = models.TextField()
    product_full_description = models.TextField()
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product_category")
    product_price = models.CharField(max_length=255)
    product_Image_Field = models.ImageField(upload_to=upload_image_path,null=True,blank=False)
    Active = models.BooleanField(default=True)
    featured_product = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now, editable=False)
    
    slug = models.SlugField(blank=True,unique=True)
    objects = ProductManager()
    def __str__(self):
        return self.product_title
    
    def get_percentage_off(self):
        newmoriginal = self.product_price - self.product_discount_price
        percentage = (newmoriginal/self.product_price) * 100
        return int(percentage)
    def new_products(self):
        original_date = self.created_date
        subtracteddate = original_date - now()

        return subtracteddate
    
    def return_two_weeks(self):
        two_weeks = datetime.timedelta(hours=336)
        return two_weeks
    def vendor_absolute_url(self):
        return reverse("vendors:product_detailed", kwargs={
            'id': self.id
        })

    def get_product_view(self):
        return reverse("farmers:product_view", kwargs={
            'id': self.id
        })

    def vendor_get_product_view(self):
        return reverse("vendors:product_view", kwargs={
            'id': self.id
        })

    def resell_product(self):
        return reverse("vendors:add_product", kwargs={
            'id': self.id
        })

    
class ProductImage(models.Model):
    product_id =  models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product_image")
    product_Image_Field = models.ImageField(upload_to=upload_image_path,null=True,blank=False)

class ProductDiscount(models.Model):
    product_id =  models.ForeignKey(Products,on_delete=models.CASCADE,related_name="discount_id")
    dicount_name =  models.CharField(max_length=255)
    dicount_discription =  models.TextField()
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active =  models.BooleanField(default=False)
    created_at =  models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.dicount_name

    def get_percentage_off(self):
        percentage_discount = self.discount_percentage
        original_price = self.product_id.product_price
        calc = (percentage_discount * original_price)/100
        mn =  calc + original_price
        dicti = {}
        dicti['new_price'] = mn
        dicti['original_price'] = original_price
        dicti['percentage'] = percentage_discount
        return dicti
class ProductQuantity(models.Model):
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="inventory_id")
    initial_quantity = models.DecimalField(max_digits=10,decimal_places=2)
    remaining_qty =  models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    final_quantity =  models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(default=now ,editable=False)


    def __str__(self):
        return str(self.initial_quantity)
  



def product_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_presave_reciver,sender = Products)

def category_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = category_unique_slug_generator(instance)


pre_save.connect(category_presave_reciver,sender = Category)

# class PostImage(models.Model):
#     product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
#     more_images = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

#     def __str__(self):
#         return self.product.product_title

# class MoreProductQuantirty(models.Model):
#     product_more = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
#     more_product_quantity = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)

#     def __str__(self):
#         return self.product_more.product_title









    
