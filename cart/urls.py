from django.urls import path

from cart.views import CartView, RemoveCartItem

app_name = 'cart'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    # path('add-to-cart/<slug>/', AddToCart.as_view(), name='add_to_cart'),
    path('remove/<pk>/', RemoveCartItem.as_view(), name='remove_item_cart'),
    # path('update/', CartUpdateView.as_view(), name='cart_update'),
]
