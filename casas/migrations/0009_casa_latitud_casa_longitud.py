# Generated by Django 4.1.7 on 2023-05-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casas', '0008_rename_producto_imagencasa_casa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='latitud',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='casa',
            name='longitud',
            field=models.CharField(max_length=50, null=True),
        ),
    ]