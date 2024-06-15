# Generated by Django 5.0.3 on 2024-06-15 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('pedido', '0003_pedido_combos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='endereco',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]