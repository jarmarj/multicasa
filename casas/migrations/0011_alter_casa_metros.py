# Generated by Django 4.1.7 on 2023-05-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0010_casa_metros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='metros',
            field=models.FloatField(default=200.0),
        ),
    ]