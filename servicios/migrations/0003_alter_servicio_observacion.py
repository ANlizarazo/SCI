# Generated by Django 4.1.4 on 2023-07-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='observacion',
            field=models.CharField(max_length=300, null=True, verbose_name='Observación'),
        ),
    ]
