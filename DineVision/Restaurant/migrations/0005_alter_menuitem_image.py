# Generated by Django 3.2.11 on 2024-03-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_auto_20240301_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, storage='storages.backends.s3boto3.S3Boto3Storage', upload_to=''),
        ),
    ]