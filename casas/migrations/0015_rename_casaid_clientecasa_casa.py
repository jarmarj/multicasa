# Generated by Django 4.1.7 on 2023-05-30 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0014_rename_casa_clientecasa_casaid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientecasa',
            old_name='casaid',
            new_name='casa',
        ),
    ]
