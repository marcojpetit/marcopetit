# Generated by Django 4.2.6 on 2023-10-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entrada_entrada_etiqueta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen_portada',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
