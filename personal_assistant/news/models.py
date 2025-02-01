"""Module providing a function printing python version."""

from django.db import models
from django.contrib.auth.models import User

class NewsSummary(models.Model):
    """Class NewsSummary representing a person"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_summaries', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.title = self.title
        return self.title

class News(models.Model):
    """Class News representing a person"""
    CATEGORY_CHOICES = [
        ('finance', 'Finance'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('entertainment', 'Entertainment'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.category and self.category not in dict(self.CATEGORY_CHOICES):
            raise ValueError(f"Invalid category: {self.category}")

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.title = self.title
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title