# Generated by Django 4.1.4 on 2023-01-22 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_ciudad_nombre'),
        ('tecnico', '0004_alter_tecnico_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnico',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.ciudad', verbose_name='Ciudad'),
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
    ]
