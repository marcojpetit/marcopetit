# Generated by Django 4.2.6 on 2023-11-11 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0026_alter_entrada_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='id_autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]