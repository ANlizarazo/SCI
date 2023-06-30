# Generated by Django 4.1.5 on 2023-06-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecat', models.CharField(blank=True, max_length=60, null=True, verbose_name='Nombre Categoría')),
                ('descripcioncat', models.TextField(max_length=300, verbose_name='Descripción')),
                ('estadocat', models.CharField(blank=True, choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, null=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombrecat'],
            },
        ),
    ]
