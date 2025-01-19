from django.db import models
from django.core.validators import MinValueValidator
import datetime

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='director_general',
        verbose_name="Laboratorio asociado"
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name="Laboratorio fabricante"
    )
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(datetime.date(2015, 1, 1))],
        verbose_name="Fecha de fabricación"
    )
    p_costo = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Precio de costo"
    )
    p_venta = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Precio de venta"
    )

    def __str__(self):
        return self.nombre

