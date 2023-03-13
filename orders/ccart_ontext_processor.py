from .models import Cart , CartrDetail 


def get_or_create_cart(request):
    if request.user.is_authenticated : 
        cart = Cart.objects.get_or_create(user=request.user,status='Inprogress')
        cart_detail = CartrDetail.objects.filter(cart=cart)
        return {'cart';cart , 'cart_detail':cart_detail}

    else : 
        return {}