# Generated by Django 4.1.6 on 2023-06-29 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0002_ciudad_estado'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciudad.ciudad', verbose_name='Ciudad'),
        ),
    ]
