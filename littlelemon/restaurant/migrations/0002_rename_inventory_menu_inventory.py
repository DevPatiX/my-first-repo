# Generated by Django 5.1.2 on 2024-11-07 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='inventory',
            new_name='Inventory',
        ),
    ]
