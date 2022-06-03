from django.contrib import admin

from .models import Product, Gallery, Comment, ProductCategory, Favorite


class InlineGallery(admin.TabularInline):
    model = Gallery


class InlineComment(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'old_price', 'current_price', 'availability', 'slug']
    inlines = [InlineGallery, InlineComment]


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'created', 'product_rating', 'is_active']


admin.site.register(Comment, CommentAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent', 'active']


admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(Favorite)


