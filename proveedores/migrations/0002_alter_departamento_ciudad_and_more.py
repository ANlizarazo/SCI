# Generated by Django 4.1.4 on 2023-01-18 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.ciudad', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.departamento', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.material', verbose_name='Material'),
        ),
    ]