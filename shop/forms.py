from django import forms

from shop.models import Comment, Favorite


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['product_rating', 'comment']


class AddFavoriteItemForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = []
