# Generated by Django 5.0.3 on 2024-06-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='especializacao',
            field=models.CharField(choices=[('pizza', 'Pizza'), ('carnes', 'Carnes'), ('massas', 'Massas')], max_length=10),
        ),
    ]
