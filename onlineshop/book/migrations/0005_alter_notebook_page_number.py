# Generated by Django 5.0.4 on 2024-04-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_notebook_image_alter_notebook_page_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='page_number',
            field=models.CharField(blank=True, choices=[('40', '40'), ('60', '60'), ('80', '80'), ('100', '100'), ('200', '200')], null=True),
        ),
    ]
