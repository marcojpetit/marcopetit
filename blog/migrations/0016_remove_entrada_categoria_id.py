# Generated by Django 4.2.6 on 2023-11-10 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_entrada_categoria_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='categoria_id',
        ),
    ]
