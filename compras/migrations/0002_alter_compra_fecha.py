# Generated by Django 4.1.4 on 2023-06-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha'),
        ),
    ]
