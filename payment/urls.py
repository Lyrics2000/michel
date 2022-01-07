from os import name
from django.urls import path

from .views import (

    lipa_na_mpesa_online,

    mpesa_queyr,
    startmpesaRequest,
    lipa_na_mpesa_online_customer,
    startmpesaRequest_customer,
    mpesa_queyr_customer
   
)

app_name = "mpesa"
urlpatterns = [
 
    path('online/lipa', lipa_na_mpesa_online, name='lipa_na_mpesa'),

    path('mpesa_query/',mpesa_queyr,name="mpesa_qury"),
    path('startMpesaRequest',startmpesaRequest,name="start_mpesa"),
    path("lipa_na_mpesa/customer/",lipa_na_mpesa_online_customer,name="lipa_na_mpesa_online_customer"),
    path("start_mpesa_req/",startmpesaRequest_customer,name="startmpesaRequest_customer"),
    path("mpesa_queyr_customer/",mpesa_queyr_customer,name="mpesa_queyr_customer")
   

]

