# Generated by Django 4.1.4 on 2023-07-01 17:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha')),
                ('cantidadProducto', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Producto')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('totalCompra', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total')),
                ('valorUnidad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Producto Unidad')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['id'],
            },
        ),
    ]
