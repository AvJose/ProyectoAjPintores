from django.db import models

# Create your models here.
class Trabajos_realizados(models.Model):

    lugares = models.CharField (max_length=40)
    obras = models.CharField (max_length=40)
    tiempo = models.CharField (max_length=40)


class Materiales(models.Model):
    pinturerias = models.CharField (max_length=40)
    pinturas = models.CharField (max_length=40)
    herramientas = models.CharField (max_length=40)

class Nosotros(models.Model):
    inicio = models.CharField (max_length=40)
    especialidades = models.CharField (max_length=40)
    comotrabajamos = models.CharField (max_length=40)

class Contacto(models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    email = models.EmailField (max_length=40)
    presupuesto = models.CharField (max_length=40)

class Admin(models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    