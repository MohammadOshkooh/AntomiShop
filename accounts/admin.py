from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = UserAdmin.list_display + ('age', 'gender')
    list_filter = UserAdmin.list_filter + ('age', 'gender')
    search_fields = UserAdmin.search_fields + ('age', 'gender')
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", 'gender')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age",'gender')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
