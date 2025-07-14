from .product_viewset import ProductViewSet
from .category_viewset import CategoryViewSet


from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers.category_serializer import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class=CategorySerializer
    def queryset(self):
        return Category.objects.all().order_by("id")
