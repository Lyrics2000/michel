from django.contrib import admin
from django.db import models
from .models import MpesaQueryCustomer, MpesaResquest,MpesaQuery, MpesaResquestCustomer,Paid, PaidCustomer




class MpesaLipaAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'user_id','cart_id','chechoutrequestid','responsecode','responsedescription']
    class Meta:
        model = MpesaResquest



admin.site.register(MpesaResquest,MpesaLipaAdmin)


class MpesaQueryAdmin(admin.ModelAdmin):
    list_display = ['__str__' ,'mpesa_request_id', 'response_code','response_description','merchant_id','checkout_request_id','result_code','result_description','status','request_id']
    class Meta:
        model = MpesaQuery

admin.site.register(MpesaQuery,MpesaQueryAdmin)
admin.site.register(Paid)




# customer

class MpesaLipaAdminCustomer(admin.ModelAdmin):
    list_display = ['__str__' , 'user_id','cart_id','chechoutrequestid','responsecode','responsedescription']
    class Meta:
        model = MpesaResquestCustomer



admin.site.register(MpesaResquestCustomer,MpesaLipaAdminCustomer)


class MpesaQueryAdminCustomer(admin.ModelAdmin):
    list_display = ['__str__' ,'mpesa_request_id', 'response_code','response_description','merchant_id','checkout_request_id','result_code','result_description','status','request_id']
    class Meta:
        model = MpesaQueryCustomer

admin.site.register(MpesaQueryCustomer,MpesaQueryAdminCustomer)
admin.site.register(PaidCustomer)









