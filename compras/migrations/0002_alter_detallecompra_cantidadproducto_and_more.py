# Generated by Django 4.1.4 on 2023-06-30 15:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidadProducto',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotalCompra',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Subtotal'),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='valorTotalProducto',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Producto Unidad'),
        ),
    ]