from rest_framework import serializers 
from .models import Product , Brand 



class BrandSerializers (serializers.ModelSerializer) : 
    class Meta : 
        model = Brand 
        fields = '__all__' 


class ProductSerializer (serializers.ModelSerializer) : 
    #brand = BrandSerializers () #show all brand details 
    brand = serializers.StringRelatedField #show brand name only 
    class Meta : 
        model = Product 
        fields = '__all__' 


