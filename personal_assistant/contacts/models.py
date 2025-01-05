"""Module providing a function printing python version."""

from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Contact(models.Model):
    """Class Contact representing a person"""
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r"^\+?1?\d{9,15}$", "Некоректний формат номера телефону")
        ],
    )
    email = models.EmailField(validators=[EmailValidator("Некоректний формат email")])
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        """__str__ returns <type 'str'>"""
        self.name = self.name
        return self.name
