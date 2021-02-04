from django.db import models
from preguntas.models import Pregunta
from solicitud_encuesta.models import Solicitud

class Respuesta(models.Model):
    tipo_respuesta = models.CharField(max_length= 20,  default="Seleccione tipo de pregunta")
    respuesta = models.TextField(default="Responder")  
    
    def __str__(self):
        return self.respuesta

class Vinculacion_respuesta(models.Model):
    id_respuesta  = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
    id_pregunta  = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_solicitud  = models.ForeignKey(Solicitud, on_delete=models.CASCADE)



