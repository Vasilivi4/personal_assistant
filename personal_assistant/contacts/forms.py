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
    number = forms.IntegerField(required=False, label='Month')
    days = forms.IntegerField(required=False, label='Days')


class ContactSearchForm(forms.Form):
    query = forms.CharField(required=False)
    number = forms.IntegerField(required=False, min_value=1, max_value=12)
    days = forms.IntegerField(required=False, min_value=0)
    class Meta:
        """Class Meta representing a person"""
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'birthday']

    def clean_phone(self):
        """Function clean_phone printing python version."""
        phone = self.cleaned_data['phone']
        if not phone.startswith('+'):
            raise forms.ValidationError("Номер телефона должен начинаться с '+'")
        return phone