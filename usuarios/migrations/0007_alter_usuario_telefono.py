# Generated by Django 4.1.4 on 2023-01-21 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Teléfono'),
        ),
    ]
