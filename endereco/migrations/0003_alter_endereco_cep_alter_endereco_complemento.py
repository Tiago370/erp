# Generated by Django 5.0.3 on 2024-03-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_alter_endereco_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
