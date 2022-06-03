from django.contrib.auth.decorators import login_required

from cart.models import Cart
from shop.models import Favorite, ProductCategory


def context_processors(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(owner=user, is_paid=False).first()
        favorite_list = Favorite.objects.filter(owner=user).first()
        return {
            'cart': cart,
            'favorite_list': favorite_list,
        }
    return {

    }
