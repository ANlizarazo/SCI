# Generated by Django 3.0 on 2023-01-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0005_alter_tecnico_ciudad_delete_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnico',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
