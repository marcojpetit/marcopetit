# Generated by Django 4.2.6 on 2023-11-10 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_entrada_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id_categoria',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='blog.categoria'),
            preserve_default=False,
        ),
    ]
