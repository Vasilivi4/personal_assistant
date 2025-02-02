"""This module registers the Note and Tag models with the Django admin site."""

from django.contrib import admin
from notes.models import Note, Tag

admin.site.register(Note)
admin.site.register(Tag)
