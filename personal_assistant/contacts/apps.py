"""Module providing a function printing python version."""

from django.apps import AppConfig


class ContactsConfig(AppConfig):
    """Class ContactsConfig representing a person"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "contacts"
