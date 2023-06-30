# Generated by Django 4.1.5 on 2023-06-30 00:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('clientes', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto')),
                ('valorTotalProducto', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total Producto')),
                ('modoPago', models.CharField(choices=[('EF', 'Efectivo'), ('PV', 'Pago Virtual'), ('PT', 'Pago con Tarjeta')], default='EF', max_length=3, verbose_name='Modo de Pago')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalles de Ventas',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotalVenta', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Subtotal Venta')),
                ('fecha', models.DateTimeField(help_text='MM/DD/AAAA', verbose_name='Fecha Venta')),
                ('porcentajeIva', models.DecimalField(decimal_places=1, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Porcentaje IVA')),
                ('totalVenta', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total Venta')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente')),
                ('detalleVenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.detalleventa', verbose_name='Detalle Venta')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio', verbose_name='Servicio')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['fecha'],
            },
        ),
    ]
