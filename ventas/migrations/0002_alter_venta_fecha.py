# Generated by Django 4.1.4 on 2023-07-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]
