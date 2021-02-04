import datetime
from django.db import models
from django.utils import timezone


# PREGUNTAS 
class Pregunta(models.Model):
    texto_pregunta = models.TextField(default= "Escribir Pregunta") 
    tipo_pregunta = models.TextField(default="Ingrese Tipo de pregunta")  
    alternativa = models.TextField(default="Ingrese las alternativas")  
    estado = models.CharField(max_length=20, default="Seleccione el estado de la pregunta") 
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.texto_pregunta
    def was_published_recently(self):
        return self.pub_date >= timezone.now() 
datetime.timedelta(days=1)

class Topico(models.Model):
    topic = models.CharField(max_length= 200, default="Escribir el topico de la encuesta")

class Pregunta_topico(models.Model):
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    topico_id = models.ForeignKey(Topico, on_delete=models.CASCADE)