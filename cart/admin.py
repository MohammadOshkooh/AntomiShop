from django.contrib import admin

from cart.models import Cart, Item


class ItemInline(admin.TabularInline):
    model = Item


class CartAdmin(admin.ModelAdmin):
    list_display = ['owner', 'creation_date', 'is_paid']
    inlines = [ItemInline]


admin.site.register(Cart, CartAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'price', 'quantity']


admin.site.register(Item, ItemAdmin)
