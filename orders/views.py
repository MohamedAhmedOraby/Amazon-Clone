from django.shortcuts import render
from .models import Order
from django.views.generic import ListView 


class OrderList (ListView) : 
    model = Order 

    def get_queryset(self):
        data = Order.objects.filter(user=self.request.user)
        return data 
    


     