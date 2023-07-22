# Generated by Django 4.1.4 on 2023-07-20 05:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='cantidadProducto',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto'),
        ),
    ]
