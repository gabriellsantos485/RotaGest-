# Generated by Django 5.1.4 on 2025-03-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usu_isAdmin',
            field=models.BooleanField(default=0, verbose_name='Administrador'),
        ),
    ]
