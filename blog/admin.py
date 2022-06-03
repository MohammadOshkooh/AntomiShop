from django.contrib import admin

from blog.models import Article, BlogComment, Gallery, ArticleCategory


class InlineComment(admin.TabularInline):
    model = BlogComment


class InlineGallery(admin.TabularInline):
    model = Gallery


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    inlines = [InlineComment, InlineGallery]


admin.site.register(Article, ArticleAdmin)

admin.site.register(ArticleCategory)


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'article', 'is_active', 'created', 'comment']


admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(Gallery)
