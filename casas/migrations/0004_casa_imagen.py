# Generated by Django 4.1.7 on 2023-05-15 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0003_casa_vendida'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]