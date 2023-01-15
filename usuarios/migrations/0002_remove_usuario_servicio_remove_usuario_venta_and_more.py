# Generated by Django 4.1.4 on 2023-01-15 22:10

from django.db import migrations, models


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
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='images/usuarios/default.png', upload_to='images/usuarios'),
        ),
    ]
