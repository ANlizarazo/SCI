# Generated by Django 4.1.4 on 2023-07-06 03:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0001_initial'),
        ('servicios', '0003_alter_servicio_valortotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciudad.ciudad', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='porcentajeIva',
            field=models.DecimalField(choices=[('5', 'Bienes y Servicios'), ('0', 'Exento')], decimal_places=1, default='5', max_digits=20, max_length=2, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='IVA'),
        ),
    ]
