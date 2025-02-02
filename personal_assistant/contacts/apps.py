"""This module contains the ContactsConfig class representing a person."""

from django.apps import AppConfig


class ContactsConfig(AppConfig):
    """Class ContactsConfig representing a person"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "contacts"
