# Generated by Django 4.1.4 on 2023-07-24 23:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('productos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha')),
                ('cantidadProducto', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto')),
                ('valorUnidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Unidad')),
                ('modoPago', models.CharField(choices=[('EF', 'Efectivo'), ('PV', 'Pago Virtual'), ('PT', 'Pago con Tarjeta')], default='EF', max_length=3, verbose_name='Modo de Pago')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('porcentajeIva', models.CharField(choices=[('5', 'Bienes y Servicios'), ('19', 'General'), ('0', 'Exento')], default='19', max_length=3, verbose_name='IVA')),
                ('valorTotal', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total')),
                ('subTotal', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Subtotal')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalles de Ventas',
                'ordering': ['fecha'],
            },
        ),
    ]
