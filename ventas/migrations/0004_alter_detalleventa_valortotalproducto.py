# Generated by Django 4.1.4 on 2023-01-20 03:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_alter_detalleventa_options_alter_venta_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='valorTotalProducto',
            field=models.DecimalField(decimal_places=1, max_digits=50, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Valor Total Producto'),
        ),
    ]