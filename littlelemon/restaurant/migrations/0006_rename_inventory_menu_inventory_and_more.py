# Generated by Django 5.1.1 on 2024-11-12 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='Inventory',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Title',
            new_name='title',
        ),
    ]
