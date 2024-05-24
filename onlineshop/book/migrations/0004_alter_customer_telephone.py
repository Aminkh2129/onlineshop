# Generated by Django 5.0.4 on 2024-05-12 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_customer_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Telephone',
            field=models.CharField(blank=True, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+983456789'. Up to 11 digits allowed.", regex='^(\\+98|0)?9\\d{9}$')]),
        ),
    ]
