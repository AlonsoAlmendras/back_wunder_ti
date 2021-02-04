from django.db import models
from encuesta.models import Encuesta
from perfil_cliente.models import Usuario_cliente
from perfil_wunder.models import Usuario_wunder

import datetime
from django.utils import timezone
# Create your models here.

class Solicitud(models.Model):
    id_encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Usuario_cliente, on_delete=models.CASCADE)
    id_wunder = models.ForeignKey(Usuario_wunder, on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fecha envío solicitud')
    estado = models.CharField(max_length=20, default="Seleccione el estado de la pregunta solicitud") 
    puntaje_obtenido = models.DecimalField(max_digits=6, decimal_places=3)

    def was_published_recently(self):
        return self.fecha >= timezone.now() 
datetime.timedelta(days=1)