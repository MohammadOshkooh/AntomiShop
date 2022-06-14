from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializers, ProductCategorySerializer

from shop.models import Product, ProductCategory


# class ProductList(ListAPIView):
#     queryset = Product.objects.filter(availability=True)
#     serializer_class = ProductSerializers


# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.filter(availability=True)
#     serializer_class = ProductSerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(availability=True)
    serializer_class = ProductSerializers

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_class = [AllowAny]
        else:
            permissions_class = [IsAdminUser]
        return [permission() for permission in permissions_class]


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_class = [AllowAny]
        else:
            permissions_class = [IsAdminUser]
        return [permission() for permission in permissions_class]
