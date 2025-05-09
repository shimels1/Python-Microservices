from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .models import User
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
import random
from .producer import publish

class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        publish()
        return Response(serializer.data)

    def create(self,requests):
        serializer = ProductSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self,request,pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    def destroy(self,request,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id':user.id
        })
