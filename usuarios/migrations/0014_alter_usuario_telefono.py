# Generated by Django 4.1.4 on 2023-03-03 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_alter_usuario_genero_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.BigIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Teléfono'),
        ),
    ]
