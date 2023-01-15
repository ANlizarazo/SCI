# Generated by Django 4.1.4 on 2023-01-14 23:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadMaterial', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Material')),
                ('valorTotalMaterial', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Total Material')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor')),
            ],
        ),
    ]
