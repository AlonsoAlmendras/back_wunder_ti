from django.db import models
from preguntas.models import Pregunta
from preguntas.models import Topico

# Create your models here.

# ENCUESTA
class Encuesta(models.Model):
    nombre_encuesta = models.CharField(max_length= 200, default="Escribir el nombre de la encuesta")
    texto_encuesta  = models.TextField(default="Ingresar descripción de la encuesta.")
    puntaje_total = models.IntegerField(default="Ingresar puntaje total de la encuesta.")
    def __str__(self):
        return self.nombre_encuesta

class Posee(models.Model):
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    encuesta_id = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    importancia_pregunta = models.IntegerField(default="Ingresar peso de la pregunta en la encuesta. (En porcentaje: 20,30 etc)")

class Encuesta_topico(models.Model):
    encuesta_id = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    topico_id = models.ForeignKey(Topico, on_delete=models.CASCADE)

