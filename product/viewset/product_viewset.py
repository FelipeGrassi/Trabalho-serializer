
from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    def queryset(self):
        return Product.objects.all()
