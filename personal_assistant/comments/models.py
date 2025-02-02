"""Comment models."""

from django.db import models
from news.models import Post

class Comment(models.Model):
    """Class Comment representing a person."""
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """__str__ returns <type 'str'>."""
        return str(self.text)[:50]