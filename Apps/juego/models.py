from django.db import models
from django.utils.html import format_html
from .seleccionar import sexos
#from seleccionar import sexos

# Create your models here.

class Tematica(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre

# --------------------------------------------------------------------------------------------

class Pregunta(models.Model):
    texto = models.CharField(max_length=150)
    tematica = models.ForeignKey(Tematica, null=False, default=1, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.texto

# --------------------------------------------------------------------------------------------

class Respuesta(models.Model):
    texto = models.CharField(max_length=80)
    pregunta = models.ForeignKey(Pregunta, null=False, default=1, on_delete=models.RESTRICT)
    correcta = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.texto   

# --------------------------------------------------------------------------------------------



# ===================================================================


