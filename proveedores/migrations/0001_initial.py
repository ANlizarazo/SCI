# Generated by Django 4.1.4 on 2023-06-30 02:42

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
                ('email', models.CharField(max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudad.ciudad', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombreEmpresa'],
            },
        ),
    ]
