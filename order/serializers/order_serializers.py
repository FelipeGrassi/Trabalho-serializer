from itertools import product

from rest_frameworl import serializers
from product.models import Product
from product.serializers.product_serializer importe ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(required=True,many=True)
    total=serializers.SerializerMethodFiels()

    def get_total(selfself,instance):
        total=sum([product.price for product in instance.product.all()])
        return total
    class Meta:
        model=product
        fields=["product","total"]
