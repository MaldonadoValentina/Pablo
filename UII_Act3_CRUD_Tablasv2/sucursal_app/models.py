from django.db import models
from django.core.validators import RegexValidator


# Sucursal
class Sucursal(models.Model):
    idSucursal = models.CharField(primary_key=True, max_length=6)
    nombre_sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    horaApertura = models.TimeField()
    horaCierre = models.TimeField()
    nombre_encargado = models.CharField(max_length=100)
    cp = models.CharField(
        max_length=10,  # Suficiente para CPs internacionales
        validators=[
            RegexValidator(
                regex=r'^\d{5}(-\d{4})?$',
                message="El código postal debe tener 5 dígitos."
            )
        ]
    )
    numero_telefono_s = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r'^\+?1?\d{9,15}$',
                message="El número debe ser entre 9 y 15 dígitos, y puede incluir '+' al inicio."
            )
        ]
    )

    def __str__(self):
        return self.nombre_sucursal


# Provedor
class Provedor(models.Model):
    idProvedor = models.CharField(primary_key=True, max_length=6)
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    calificacion = models.IntegerField()
    correo = models.EmailField(max_length=254)
    ciudad = models.CharField(max_length=50)
    numero_telefono_p = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                r'^\+?1?\d{9,15}$',
                message="El número debe ser entre 9 y 15 dígitos, y puede incluir '+' al inicio."
            )
        ]
    )

    def __str__(self):
        return self.nombre_empresa
