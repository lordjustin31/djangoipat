# Generated by Django 5.0.6 on 2024-07-07 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_name_item_first_name_remove_item_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='address',
        ),
        migrations.RemoveField(
            model_name='item',
            name='email',
        ),
        migrations.RemoveField(
            model_name='item',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='phone',
        ),
    ]
