from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "address", "phone", "email", "birthday"]


class ContactSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Пошук")
