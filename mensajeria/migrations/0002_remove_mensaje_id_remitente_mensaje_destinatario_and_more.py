# Generated by Django 4.2.6 on 2023-11-11 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='id_remitente',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='destinatario',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
