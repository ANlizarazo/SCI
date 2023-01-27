# Generated by Django 4.1.4 on 2023-01-14 23:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nit', models.CharField(max_length=20, unique=True, verbose_name='NIT')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electrónico')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.ciudad', verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto')),
                ('valorTotalProducto', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total Producto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTotalVenta', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Subtotal Venta')),
                ('fecha', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S')),
                ('porcentajeIva', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Porcentaje IVA')),
                ('totalVenta', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Total Venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente', verbose_name='Cliente')),
                ('detalleVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.detalleventa', verbose_name='Detalle Venta')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.compra', verbose_name='Compra'),
        ),
    ]
