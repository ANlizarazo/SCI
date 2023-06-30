# Generated by Django 4.1.4 on 2023-06-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_alter_servicio_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]