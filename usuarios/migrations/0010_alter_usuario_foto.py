# Generated by Django 4.1.4 on 2023-02-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='/static/img/perfil.jpg', upload_to='images/usuarios'),
        ),
    ]
