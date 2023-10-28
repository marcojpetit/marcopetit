# Generated by Django 4.2.6 on 2023-10-28 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('contenido', models.TextField()),
                ('id_autor', models.IntegerField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('imagen_portada', models.ImageField(upload_to='')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada_etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.entrada')),
                ('id_etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.etiqueta')),
            ],
        ),
    ]
