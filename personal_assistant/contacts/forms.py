"""Module forms.py representing a person."""
# Version: 2021.09.13

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
    query = forms.CharField(required=False)
    number = forms.IntegerField(required=False, min_value=1, max_value=12)
    days = forms.IntegerField(required=False, min_value=0)

    class Meta:
        """Class Meta representing a person"""

        model = Contact
        fields = ["name", "address", "phone", "email", "birthday"]

    def clean_phone(self):
        """clean_phone returns phone"""
        phone = self.cleaned_data["phone"]
        if not phone.startswith("+"):
            raise forms.ValidationError("Номер телефона должен начинаться с '+'")
        return phone
