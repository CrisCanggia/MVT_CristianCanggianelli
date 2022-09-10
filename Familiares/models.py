from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)   
    apellido = models.CharField(max_length=40)    
    fecNac = models.DateField()
    email = models.EmailField()
    fechaAlta = models.DateTimeField(default=timezone.now)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()
    