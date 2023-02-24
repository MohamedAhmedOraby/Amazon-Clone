from django.contrib import admin
from .models import Product , ProductImages , ProductReview , Brand

class ProductImagesInLine (admin.TabularInline):
    model = ProductImages 

class ProductAdmin (admin.ModelAdmin) :
    inlines = [ProductImagesInLine]

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Brand)

