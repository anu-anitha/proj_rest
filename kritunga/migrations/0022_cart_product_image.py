# Generated by Django 4.0.1 on 2022-04-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kritunga', '0021_alter_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
