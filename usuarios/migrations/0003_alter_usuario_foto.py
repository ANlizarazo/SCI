# Generated by Django 4.1.4 on 2023-07-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, default='/static/img/perfil.jpg', null=True, upload_to='images/usuarios'),
        ),
    ]
