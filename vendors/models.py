from django.db import models
from account.models import User
import random
import os
from django.db.models import Q, base
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from products.models import Products
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


class ResellProduct(models.Model):
    product =  models.ForeignKey(Products,on_delete=models.CASCADE)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    product_price = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to=upload_image_path,null=True,blank=False)
    Active = models.BooleanField(default=True)
    featured_product = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)


    def customer_absolute_url(self):
        return reverse("customers:product_detailed", kwargs={
            'id': self.id
        })



