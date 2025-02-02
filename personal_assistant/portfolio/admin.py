"""This module contains the admin configuration for the portfolio app."""

from django.contrib import admin
from .models import Project

admin.site.register(Project)
