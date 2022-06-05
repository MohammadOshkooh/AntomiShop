from itertools import product

from django.contrib import messages
from django.shortcuts import redirect

from cart.forms import AddToCartForm
from cart.models import Cart
from shop.models import Favorite


def context_processors(request):
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(owner=user, is_paid=False).first()
        favorite_list = Favorite.objects.filter(owner=user).first()
        if request.method == 'POST':
            # add to cart
            add_to_cart_form = AddToCartForm(data=request.POST)
            if add_to_cart_form.is_valid():
                add_to_cart_form = add_to_cart_form.save(commit=False)
                cart = Cart.objects.filter(owner=user, is_paid=False).first()
                # check cart is exist
                if cart is None or cart.is_paid is True:
                    cart = Cart.objects.create(owner=user)
                add_to_cart_form.cart = cart
                add_to_cart_form.product = product
                add_to_cart_form.price = product.current_price
                add_to_cart_form.save()
                messages.success(request, 'محصول با موفقیت به سبد خرید اضافه شد')
                return redirect(product.get_absolute_url(), product.slug)
        else:
            add_to_cart_form = AddToCartForm()

        return {
            'cart': cart,
            'favorite_list': favorite_list,
            'add_to_cart_form': add_to_cart_form,
        }
    return {

    }
