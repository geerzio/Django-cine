from django.db import models

# Create your models here.


class directores(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    edad = models.CharField(max_length=10)
    
    
    
    
    
    
class peliculas(models.Model):
    director = models.ForeignKey(directores, null=False, blank=False ,on_delete=models.CASCADE)   
    nombre_de_pelicula = models.CharField(max_length=10, primary_key=True)
    año_de_pelicula = models.CharField(max_length=10) 
    genero = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    