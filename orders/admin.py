from django.contrib import admin

# Register your models here.
from .models import Order , OrderDetail , Cart , CartrDetail , Coupon

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartrDetail)
admin.site.register(Coupon)
