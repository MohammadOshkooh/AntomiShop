from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

app_name = 'shop_api'

router = routers.SimpleRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = [
    # path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    # path('', ProductList.as_view(), name='list'),

    path('', include(router.urls)),
]
