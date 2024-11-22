# Generated by Django 5.1.3 on 2024-11-22 05:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_sucursal', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('horaApertura', models.TimeField()),
                ('horaCierre', models.TimeField()),
                ('nombre_encargado', models.CharField(max_length=100)),
                ('cp', models.IntegerField()),
                ('numeroTelefono', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="El número debe ser entre 9 y 15 dígitos, y puede incluir '+' al inicio.")])),
            ],
        ),
    ]
