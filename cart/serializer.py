from django.db.models import fields
from rest_framework import serializers
from .models import Cart




class GetAllCart(serializers.ModelSerializer):
    class Meta:
        model =  Cart
        fields = "__all__"
        depth = 1