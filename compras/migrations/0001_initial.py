# Generated by Django 4.1.5 on 2023-06-30 00:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorTotalMaterial', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total Material')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalle de Compras',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('estado', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, null=True, verbose_name='Estado')),
                ('detalleCompra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.detallecompra', verbose_name='Detalle Compra')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['fecha'],
            },
        ),
    ]
