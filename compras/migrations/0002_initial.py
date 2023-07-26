# Generated by Django 4.1.6 on 2023-07-24 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compras', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor'),
        ),
    ]
