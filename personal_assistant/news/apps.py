"""This module contains the NewsConfig class representing a person."""

# Version: 1.0

from django.apps import AppConfig


class NewsConfig(AppConfig):
    """Class NewsConfig representing a person"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "news"
