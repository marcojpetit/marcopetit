# Generated by Django 4.2.6 on 2023-11-11 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_entrada_sub_titulo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entrada_etiqueta',
        ),
    ]