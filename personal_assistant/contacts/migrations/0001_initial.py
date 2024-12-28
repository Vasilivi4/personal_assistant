import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Некоректний формат номера телефону')])),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('Некоректний формат email')])),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
