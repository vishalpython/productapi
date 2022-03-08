from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import views, status

from .serializers import ProductSerializers
from rest_framework import permissions, authentication
from .models import Product
from .permissionsmixin import PermissionView
from drf_yasg.openapi import (
    Parameter,
    IN_QUERY,
    TYPE_STRING,
)
from drf_yasg.utils import swagger_auto_schema



# Create your views here.
class ProductViewset(viewsets.ViewSet):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,PermissionView)

    def list(self, request):
        product_object = Product.objects.all()
        serializer = ProductSerializers(product_object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        product_serializer = ProductSerializers(data=request.data,many=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializers(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product_obj = Product.objects.get(id=pk)
        product_serializer = ProductSerializers(product_obj, data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        product_obj = Product.objects.get(id=pk)
        product_serializer = ProductSerializers(product_obj,data=request.data,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product_obj = Product.objects.get(id=pk)
        product_obj.delete()

        return Response({'product_obj':"deleted"}, status=status.HTTP_206_PARTIAL_CONTENT)



