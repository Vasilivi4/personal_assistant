"""Module providing a function printing python version."""

from django import forms
from contacts.models import Contact


class ContactForm(forms.ModelForm):
    """Class ContactForm representing a person"""
    class Meta:
        """Class Meta representing a person"""
        model = Contact
        fields = ["name", "address", "phone", "email", "birthday"]


class ContactSearchForm(forms.Form):
    """Class ContactSearchForm representing a person"""
    query = forms.CharField(max_length=100, required=False, label="Пошук")
