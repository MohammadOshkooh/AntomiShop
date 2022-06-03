from django.contrib import admin

from tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Tag, TagAdmin)
