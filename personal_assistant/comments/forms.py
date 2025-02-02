"""This module contains the CommentForm class, which is a form for the Comment model."""

from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
    """A form for the Comment model."""
    class Meta:
        """A class representing the metadata of the CommentForm class."""
        model = Comment
        fields = ['text']
