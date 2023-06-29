# Generated by Django 4.1.4 on 2023-01-20 03:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_remove_cliente_ciudad_remove_cliente_compra_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name': 'Detalle Venta', 'verbose_name_plural': 'Detalle de Ventas'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ['fecha'], 'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='valorTotalProducto',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Valor Total Producto'),
        ),
    ]
