"""Module providing a function printing python version."""

from django.contrib import admin
from comments.models import Post  # Импорт модели Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']


admin.site.register(Post, PostAdmin)

