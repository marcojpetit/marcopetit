# Generated by Django 4.2.6 on 2023-11-10 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_entrada_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria'),
        ),
    ]
