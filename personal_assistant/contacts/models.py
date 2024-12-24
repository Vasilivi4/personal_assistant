from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Contact(models.Model):
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
        return self.name
