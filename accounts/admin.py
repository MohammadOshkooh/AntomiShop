from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = UserAdmin.list_display + ('age', 'gender', 'Subscribe_to_the_newsletter')
    list_filter = UserAdmin.list_filter + ('age', 'gender', 'Subscribe_to_the_newsletter')
    search_fields = UserAdmin.search_fields + ('age', 'gender', 'Subscribe_to_the_newsletter')
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", 'gender', 'Subscribe_to_the_newsletter')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", 'gender', 'Subscribe_to_the_newsletter')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
