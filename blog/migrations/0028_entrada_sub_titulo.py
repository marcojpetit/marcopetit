# Generated by Django 4.2.6 on 2023-11-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_entrada_id_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='sub_titulo',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
