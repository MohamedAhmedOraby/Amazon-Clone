from django.shortcuts import render, redirect 
from .models import Order , Cart , CartrDetail 
from django.views.generic import ListView 
from product.models import Product 


class OrderList (ListView) : 
    model = Order 

    def get_queryset(self):
        data = Order.objects.filter(user=self.request.user)
        return data 
    

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        quantity = request.POST['quantity']

        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=request.user , status='Inprogress')
        cart_detail,created = CartrDetail.objects.get_or_create(
            cart=cart , 
            product = product
        )

        cart_detail.quantity = int(quantity)
        cart_detail.price = product.price
        cart_detail.total = int(quantity)* product.price
        cart_detail.save()

    return redirect(f'/products/{product.slug}')

def checkout (request): 
    return render (request,'orders/checkout.html',{})
 