# Generated by Django 4.0.3 on 2022-03-19 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kritunga', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
    ]
