# Generated by Django 4.1.7 on 2023-05-15 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0005_imagencasa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casa',
            name='imagen',
        ),
    ]
