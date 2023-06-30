# Generated by Django 4.1.6 on 2023-06-30 04:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('telefono', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Teléfono')),
                ('email', models.CharField(max_length=100, verbose_name='Correo Electrónico')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PP', 'Pasaporte'), ('OT', 'Otro')], max_length=4, verbose_name='Tipo de Documento')),
                ('numDocumento', models.CharField(max_length=20, verbose_name='Número de Documento')),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('O', 'Otro')], max_length=3, verbose_name='Género')),
                ('rol', models.CharField(choices=[('Admin', 'Administrador'), ('Empl', 'Empleado')], max_length=5, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['nombres'],
            },
        ),
    ]
