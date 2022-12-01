from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    numero_dia=models.IntegerField()


class Post(models.Model):
    post_nombre=models.CharField(max_length=40)
    post_totalcaracteres=models.IntegerField()
    post_puntaje=models.IntegerField() 


class Usuario(models.Model):
    usuario_nombre=models.CharField(max_length=40)
    usuario_apellido=models.CharField(max_length=40)
    usuario_mail=models.CharField(max_length=40)       


class Categoria(models.Model):
    categoria_nombre=models.CharField(max_length=40)
    categoria_importancia=models.IntegerField()
    categoria_descripcion=models.CharField(max_length=40)      