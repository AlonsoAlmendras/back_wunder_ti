from django.db import models

class Correos_wunder(models.Model):
    email = models.CharField(max_length=100, default="Ingrese email")
    clave = models.CharField(max_length=30, default="Ingrese clave")
    def __str__(self):
        return self.email

class Usuario_wunder(models.Model):
    nickname = models.CharField(max_length= 100, default="Escribir nombre")
    def __str__(self):
        return self.nickname

class Ingreso_wunder(models.Model):
    usuario_wunder_id = models.ForeignKey(Usuario_wunder, on_delete=models.CASCADE)
    email_wunder_id = models.ForeignKey(Correos_wunder, on_delete=models.CASCADE)