# Generated by Django 4.0.1 on 2022-05-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kritunga', '0017_orderitem_todayorders_alter_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='category_name',
        ),
    ]