# Generated by Django 5.0.1 on 2024-02-03 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_rename_name_vendor_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='is_approved',
            new_name='is_active',
        ),
    ]