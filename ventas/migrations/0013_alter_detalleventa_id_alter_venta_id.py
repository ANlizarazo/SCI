# Generated by Django 4.1.4 on 2023-01-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_auto_20230125_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]