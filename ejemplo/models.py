from django.db import models

# Create your models here.
class Familiar(models.Model):
      nombre = models.CharField(max_length=100)
      direccion = models.CharField(max_length=200)
      numero_pasaporte = models.IntegerField()

      def __str__(self):
            return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Competidor(models.Model):
      apellido = models.CharField(max_length=100)
      nombre = models.CharField(max_length=100)
      dni = models.IntegerField()
      prueba = models.CharField(max_length=100)
      emerg_contacto = models.CharField(max_length=100)
      emerg_llamar = models.IntegerField()

      def __str__(self):
            return f"{self.apellido}, {self.prueba}, {self.id}"