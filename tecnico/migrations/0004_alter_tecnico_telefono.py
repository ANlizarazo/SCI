# Generated by Django 4.1.4 on 2023-01-21 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0003_alter_ciudad_options_alter_tecnico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnico',
            name='telefono',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Teléfono'),
        ),
    ]