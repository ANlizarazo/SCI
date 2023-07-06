# Generated by Django 4.1.4 on 2023-07-06 00:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_valortotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='valorTotal',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total'),
        ),
    ]
