# Generated by Django 4.1.4 on 2023-01-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnico', '0006_auto_20230125_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnico',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]