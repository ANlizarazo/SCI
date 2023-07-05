# Generated by Django 4.1.4 on 2023-07-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=50, verbose_name='Nombre de Servicio')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripción del Servicio')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'TipodeServicio',
                'verbose_name_plural': 'TiposdeServicios',
                'ordering': ['nombreServicio'],
            },
        ),
    ]
