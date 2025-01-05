from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User


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
    birthday = models.DateField(blank=True, null=True,
                                help_text="Введіть дату у форматі РРРР-ММ-ДД, наприклад, 2000-01-01")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name
