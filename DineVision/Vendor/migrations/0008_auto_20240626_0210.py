# Generated by Django 3.2.11 on 2024-06-25 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0007_alter_vendor_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='restaurant_licence',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='restaurant_name',
        ),
    ]