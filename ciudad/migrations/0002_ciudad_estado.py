# Generated by Django 4.1.4 on 2023-06-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
    ]
