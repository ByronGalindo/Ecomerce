from django.db import models

# Create your models here.


class servicio(models.Model):
    
    NombreServicio = models.CharField(max_length=50,verbose_name='Servicio')
    ContenidoServicio = models.CharField(max_length=100, verbose_name='Contenido')
    Imagen = models.ImageField(upload_to='ServiciosApp', height_field=None, width_field=None, max_length=None, verbose_name='Imagen')
    FechaCreacionServicio = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Creado')
    FechaActualizacionServicio = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.NombreServicio
    