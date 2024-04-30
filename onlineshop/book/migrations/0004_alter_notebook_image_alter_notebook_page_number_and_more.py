# Generated by Django 5.0.4 on 2024-04-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_notebook_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='page_number',
            field=models.BigIntegerField(blank=True, choices=[('40', '40'), ('60', '60'), ('80', '80'), ('100', '100'), ('200', '200')], null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
