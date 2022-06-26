from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    title = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())
