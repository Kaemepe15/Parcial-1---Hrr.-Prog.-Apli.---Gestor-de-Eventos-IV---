from django.db import models

#Modelos: Organizador y Evento.

#Modelo Organizador

class Organizador(models.Model):
    nombre_org= models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.nombre_org

#Modelo Evento

class Evento(models.Model):
    nombre_org= models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos')
    nombre_event= models.CharField(max_length=200)
    date_event= models.DateTimeField()
    descrip_event= models.TextField()

    def __str__(self) -> str:
        return self.nombre_event

