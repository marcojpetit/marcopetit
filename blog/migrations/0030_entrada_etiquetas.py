# Generated by Django 4.2.6 on 2023-11-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_delete_entrada_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='etiquetas',
            field=models.ManyToManyField(to='blog.etiqueta'),
        ),
    ]