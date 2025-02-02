"""Admin configuration for the contacts app."""
# Version: 1.0

from django.contrib import admin
from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Class ContactAdmin representing a person"""

    list_display = ("name", "phone", "email", "birthday")
    search_fields = ("name", "email", "phone")
