"""Module providing a function printing python version."""

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Class ContactAdmin representing a person"""
    list_display = ("name", "phone", "email", "birthday")
    search_fields = ("name", "email", "phone")

