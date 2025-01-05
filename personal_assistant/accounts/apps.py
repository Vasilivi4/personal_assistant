"""Module providing a function printing python version."""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Class AccountsConfig representing a person"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
