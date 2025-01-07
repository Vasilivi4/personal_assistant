"""Module providing a function printing python version."""

from django.apps import AppConfig


class NewsConfig(AppConfig):
    """Class NewsConfig representing a person"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
