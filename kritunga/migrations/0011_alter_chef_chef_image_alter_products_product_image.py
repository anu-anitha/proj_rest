# Generated by Django 4.0.3 on 2022-04-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kritunga', '0010_rename_shef_availability_chef_chef_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='chef_image',
            field=models.ImageField(default='images', upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='images', upload_to=''),
        ),
    ]