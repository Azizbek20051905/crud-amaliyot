# Generated by Django 5.2 on 2025-07-03 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='narx',
            new_name='price',
        ),
    ]
