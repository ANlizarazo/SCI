# Generated by Django 4.1.4 on 2023-01-21 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%s'),
        ),
    ]
