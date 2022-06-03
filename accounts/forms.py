from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'gender')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


# class UpdateProfile(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name', 'last_name', 'age', 'gender']
