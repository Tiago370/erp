# Generated by Django 5.0.3 on 2024-06-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0021_alter_restaurante_especializacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='especializacao',
            field=models.CharField(choices=[('pizza', 'Pizza'), ('massas', 'Massas'), ('carnes', 'Carnes')], max_length=10),
        ),
    ]
