"""Module providing a function printing python version."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """Class RegisterForm representing a person"""
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    email = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput())

    password2 = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput())

    class Meta:
        """Class Meta representing a person"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    """Class LoginForm representing a person"""

    class Meta:
        """Class Meta representing a person"""
        model = User
        fields = ['username', 'password']