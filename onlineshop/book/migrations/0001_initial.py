# Generated by Django 5.0.4 on 2024-04-27 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('sum_price', models.BigIntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'Order_Item',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code_meli', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('Telephone', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('unit_no', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField()),
                ('status_order', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='book.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='book.order_item')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.AddField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='book.product'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_book', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=25)),
                ('publisher', models.CharField(max_length=20)),
                ('publish_date', models.DateField()),
                ('c_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_product', to='book.product')),
            ],
            options={
                'db_table': 'Category',
            },
        ),
    ]
