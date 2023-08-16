from django.db import models

# Create your models here.

class CategoriaProdcuto(models.Model):

    Nombre = models.CharField(max_length=50)
    Creada = models.DateField(auto_now_add=True)
    Actualizada = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'CategoriaProdcuto'
        verbose_name_plural = 'CategoriaProdcutos'
        
    def __str__(self):
        return self.Nombre
     
    
class Producto(models.Model):

    Nombre = models.CharField(max_length=50)
    Categorias = models.ForeignKey(CategoriaProdcuto,on_delete=models.CASCADE)
    Imagen = models.ImageField(blank=True, null=True, upload_to="TiendaApp")
    Precio = models.FloatField()
    Disponibilidad = models.BooleanField(default=True)
    Creado = models.DateField(auto_now_add=True)
    Actualizado = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Prodcuto'
        verbose_name_plural ='Productos'

    def __str__(self):
        return self.Nombre
