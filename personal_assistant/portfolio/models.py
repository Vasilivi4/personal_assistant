"""This file contains the models for the portfolio app."""

from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    """Class Project representing a project"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField("image", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.title = self.title
        return self.title
