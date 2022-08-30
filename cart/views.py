from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from cart.forms import AddToCartForm, DeleteCartItem
from cart.models import Cart, Item


class CartView(LoginRequiredMixin, FormView):
    form_class = AddToCartForm
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['update_form'] = context.get('form')
        cart = Cart.objects.filter(owner=self.request.user, is_paid=False).first()
        context['cart'] = cart
        return context

    def form_valid(self, form):
        form.save()
        return redirect('cart:cart')


class RemoveCartItem(FormView):
    form_class = DeleteCartItem

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        cart_item = Item.objects.filter(pk=pk).first()
        cart_item.delete()
        return redirect('cart:cart')
