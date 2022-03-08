from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','details','colour','size','image','is_active')
        read_only_fields = ('id',)




