# Generated by Django 4.2.6 on 2023-11-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_entrada_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen_portada',
            field=models.ImageField(default=1, upload_to='entradas'),
        ),
    ]