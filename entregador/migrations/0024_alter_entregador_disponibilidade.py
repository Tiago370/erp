# Generated by Django 5.0.3 on 2024-06-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entregador', '0023_alter_entregador_disponibilidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregador',
            name='disponibilidade',
            field=models.CharField(choices=[('disponivel', 'Disponível'), ('ocupado', 'Ocupado'), ('desativado', 'Desativado')], default='disponível', max_length=10),
        ),
    ]
