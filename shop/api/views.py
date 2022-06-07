from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializers

from shop.models import Product


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
