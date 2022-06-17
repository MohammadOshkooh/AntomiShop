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


class DeleteCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = []


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'جستجوی محصول ...'}), max_length=100)
