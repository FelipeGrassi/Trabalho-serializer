from itertools import product

from rest_frameworl import serializers
from product.models import Product
from product.serializers.product_serializer importe ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(required=True,many=True)
    product_id=serializers.PrimaryKeyRelatedFiel(queryset=Product.objects.all(),write_only=True,many=True)
    total=serializers.SerializerMethodFiels()

    def get_total(selfself,instance):
        total=sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model=product
        fields=["product","total","user","products_id"]
        extra_kwargs={"product":{"required":False}}

    def create(self, validated_data):
        product_data=validated_data.pop("products_id")
        user_data=validated_data.pop("user")

        order=Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)
            return order

