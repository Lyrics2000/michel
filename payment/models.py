from django.db import models
from rest_framework import serializers
from account.models import User
from cart.models import Cart,CartCustomer

# Create your models here.
class MpesaResquest(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    cart_id =  models.ForeignKey(Cart,on_delete=models.CASCADE)
    merchantRequestid =  models.CharField(max_length=255)
    chechoutrequestid =  models.CharField(max_length=255)
    responsecode =  models.CharField(max_length=10)
    responsedescription =  models.TextField()
    customerMessage =  models.TextField()
    status =  models.CharField(max_length=255,blank=True,null=True)
    request_id = models.CharField(max_length=255,blank=True,null=True)
    callback_url =  models.URLField(null=True,blank=True)

    def __str__(self):
        return self.merchantRequestid
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MpesaQuery(BaseModel):
    mpesa_request_id =  models.ForeignKey(MpesaResquest,on_delete=models.CASCADE)
    response_code =  models.CharField(max_length=255)
    response_description =  models.TextField()
    merchant_id =  models.CharField(max_length=255)
    checkout_request_id =  models.CharField(max_length=255)
    result_code = models.CharField(max_length=255)
    result_description =  models.TextField()
    status = models.CharField(max_length=255)
    request_id =  models.TextField()


    def __str__(self):
        return self.response_code






class Paid(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    paid =  models.BooleanField(default=False)
    processed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.cart)




# customer
class MpesaResquestCustomer(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    cart_id =  models.ForeignKey(CartCustomer,on_delete=models.CASCADE)
    merchantRequestid =  models.CharField(max_length=255)
    chechoutrequestid =  models.CharField(max_length=255)
    responsecode =  models.CharField(max_length=10)
    responsedescription =  models.TextField()
    customerMessage =  models.TextField()
    status =  models.CharField(max_length=255,blank=True,null=True)
    request_id = models.CharField(max_length=255,blank=True,null=True)
    callback_url =  models.URLField(null=True,blank=True)

    def __str__(self):
        return self.merchantRequestid
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MpesaQueryCustomer(BaseModel):
    mpesa_request_id =  models.ForeignKey(MpesaResquestCustomer,on_delete=models.CASCADE)
    response_code =  models.CharField(max_length=255)
    response_description =  models.TextField()
    merchant_id =  models.CharField(max_length=255)
    checkout_request_id =  models.CharField(max_length=255)
    result_code = models.CharField(max_length=255)
    result_description =  models.TextField()
    status = models.CharField(max_length=255)
    request_id =  models.TextField()


    def __str__(self):
        return self.response_code






class PaidCustomer(models.Model):
    cart = models.ForeignKey(CartCustomer,on_delete=models.CASCADE)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    paid =  models.BooleanField(default=False)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.cart)



