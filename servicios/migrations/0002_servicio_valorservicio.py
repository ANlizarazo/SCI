# Generated by Django 4.1.4 on 2023-07-09 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='valorServicio',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Servicio'),
        ),
    ]
