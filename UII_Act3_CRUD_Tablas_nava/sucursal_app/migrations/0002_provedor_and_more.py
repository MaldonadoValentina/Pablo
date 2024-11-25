# Generated by Django 5.1 on 2024-11-25 15:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('idProvedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField()),
                ('correo', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=50)),
                ('numero_telefono_provedor', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="El número debe ser entre 9 y 15 dígitos, y puede incluir '+' al inicio.")])),
            ],
        ),
        migrations.RenameField(
            model_name='sucursal',
            old_name='numeroTelefono',
            new_name='numero_telefono',
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='cp',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='El código postal debe tener 5 dígitos.', regex='^\\d{5}(-\\d{4})?$')]),
        ),
    ]