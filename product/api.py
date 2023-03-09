from rest_framework.decorators import api_view
from rest_framework import generics 
from rest_framework.response import Response
from .models import Product , Brand 
from .serializers import ProductListSerializer , ProductDetailSerializer , BrandSerializers , BrandDetailSerializers


@api_view(['GET'])
def product_list_api (request): 
    query = Product.objects.all ()[:20]
    data = ProductListSerializer(query,many=True).data 
    return Response ({'data':data})


class ProductListAPI (generics.ListCreateAPIView) : 
    serializer_class = ProductListSerializer 
    queryset = Product.objects.all()[:20]

class ProductDetailAPI (generics.RetrieveUpdateDestroyAPIView) : 
    serializer_class = ProductDetailSerializer 
    queryset = Product.objects.all()
    lookup_field = 'slug'


class BrandListAPI (generics.ListAPIView) : 
    serializer_class = BrandSerializers 
    queryset = Brand.objects.all()


class BrandDetailAPI (generics.RetrieveAPIView) : 
    serializer_class = BrandDetailSerializers 
    queryset = Brand.objects.all() 
    lookup_field = 'slug'
