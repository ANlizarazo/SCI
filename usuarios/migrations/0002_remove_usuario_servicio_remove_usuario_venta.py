# Generated by Django 4.1.4 on 2023-01-15 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='venta',
        ),
    ]