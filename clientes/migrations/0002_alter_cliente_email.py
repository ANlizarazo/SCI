# Generated by Django 4.1.5 on 2023-07-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True, verbose_name='Correo Electrónico'),
        ),
    ]
