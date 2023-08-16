from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class categorias(models.Model):
    
    NombreCategoria = models.CharField(max_length=50,verbose_name='Categoria')
    FechaCreacionCategoria = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Creado')
    FechaActualizacionCategoria = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.NombreCategoria
    
    

class post(models.Model):
    NombrePost = models.CharField(max_length=50,verbose_name='Post')
    ContenidoPost = models.CharField(max_length=100, verbose_name='Contenido')
    Imagen = models.ImageField(upload_to='BlogApp', height_field=None, width_field=None, max_length=None, verbose_name='Imagen', blank=True, null=True)
    AutorPost = models.ForeignKey(User, on_delete=models.CASCADE)
    Categorias = models.ManyToManyField(categorias)
    FechaCreacionPost = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Creado')
    FechaActualizacionPost = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.NombrePost
    