# Generated by Django 4.2.13 on 2024-06-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.AddField(
            model_name='item',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
