from django import forms

from cart.models import Item


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantity']


class DeleteCartItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = []