"""Admin module for the news app."""

# Django modules

from django.contrib import admin
from comments.models import Post


class PostAdmin(admin.ModelAdmin):
    """Class PostAdmin."""

    list_display = ["title", "content", "created_at"]


admin.site.register(Post, PostAdmin)
