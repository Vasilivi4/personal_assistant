"""This module contains the models for the notes app."""

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """Class Note representing a person"""

    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = models.Manager()

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.title = self.title
        return self.title


class Tag(models.Model):
    """Class Tag representing a person"""

    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = models.Manager()

    class Meta:
        """Class Meta representing a person"""

        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name="tag of username")
        ]

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.name = self.name
        return self.name
