# Generated by Django 4.0.1 on 2022-04-30 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kritunga', '0022_cart_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_image',
        ),
    ]
