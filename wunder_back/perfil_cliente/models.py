from django.db import models

class Empresa(models.Model):
    rut = models.CharField(max_length=20, default="RUT de la empresa") 
    nombre = models.CharField(max_length=100, default="Nombre de la empresa")
    telefono = models.CharField(max_length=20, default="Número de teléfono")
    personality = models.TextField(default="Personality de la empresa")
    def __str__(self):
        return self.nombre

class Usuario_cliente(models.Model):
    nombre_usuario = models.CharField(max_length= 100, default="Escribir nombre")
    clave = models.CharField(max_length= 30, default="Ingresar clave")
    correo = models.CharField(max_length= 100, default="Escribir email")
    def __str__(self):
        return self.nombre_usuario

class Ingreso_wunder(models.Model):
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario_cliente_id = models.ForeignKey(Usuario_cliente, on_delete=models.CASCADE)

class Servicios(models.Model):
    servicio = models.CharField(max_length= 50, default="Servicios")
    def __str__(self):
        return self.servicio

class Autorizacion_servicios(models.Model):
    usuario_cliente_id = models.ForeignKey(Usuario_cliente, on_delete=models.CASCADE)
    servicio_id = models.ForeignKey(Servicios, on_delete=models.CASCADE)