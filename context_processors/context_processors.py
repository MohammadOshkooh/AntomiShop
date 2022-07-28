from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from cart.forms import AddToCartForm
from cart.models import Cart
from shop.forms import SearchForm
from shop.models import Favorite, Product


def context_processors(request):
    search_form = SearchForm()
    cart = None
    favorite_list = None
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(owner=user, is_paid=False).first()
        favorite_list = Favorite.objects.filter(owner=user).first()
    if request.method == 'POST':
        # --- add to cart ---
        add_to_cart_form = AddToCartForm(data=request.POST)
        if add_to_cart_form.is_valid():
            if request.user.is_authenticated:
                user = request.user
                add_to_cart_form = add_to_cart_form.save(commit=False)
                cart = Cart.objects.filter(owner=user, is_paid=False).first()
                # check cart is exist
                if cart is None or cart.is_paid is True:
                    cart = Cart.objects.create(owner=user)
                add_to_cart_form.cart = cart
                product_id = request.POST.get('product_id')
                productt = Product.objects.get(id=product_id)
                add_to_cart_form.product = productt
                add_to_cart_form.price = productt.current_price
                add_to_cart_form.save()
                messages.success(request, 'محصول با موفقیت به سبد خرید اضافه شد')
            else:
                messages.error(request, 'لطفا وارد حساب کاربری خود شوید')
    else:
        add_to_cart_form = AddToCartForm()

    context = {
        'cart': cart,
        'favorite_list': favorite_list,
        'add_to_cart_form': add_to_cart_form,
        'search_form': search_form,
    }

    return context
