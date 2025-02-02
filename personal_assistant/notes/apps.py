"""This module contains the class NotesConfig that represents a person."""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Class NotesConfig representing a person"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"
