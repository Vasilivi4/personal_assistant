"""Forms for the portfolio app."""

from django import forms
from portfolio.models import Project


class PortfolioForm(forms.ModelForm):
    """Form for adding a new project to the portfolio."""

    class Meta:
        """Class Meta representing a person"""

        model = Project
        fields = ["title", "description", "image", "url"]
