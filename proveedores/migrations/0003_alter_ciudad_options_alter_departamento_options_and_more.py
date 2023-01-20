# Generated by Django 4.1.4 on 2023-01-20 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_alter_departamento_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['nombre'], 'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['nombre'], 'verbose_name': 'Material', 'verbose_name_plural': 'Materiales'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['nombreEmpresa'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]
