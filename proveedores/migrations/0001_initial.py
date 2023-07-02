# Generated by Django 4.1.6 on 2023-07-01 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ciudad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmpresa', models.CharField(max_length=100, verbose_name='Nombre Empresa')),
                ('nit', models.BigIntegerField(unique=True, verbose_name='NIT')),
                ('telefono', models.BigIntegerField(verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electrónico')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciudad.ciudad', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombreEmpresa'],
            },
        ),
    ]
