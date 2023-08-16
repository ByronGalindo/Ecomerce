from django.db import models
from django.contrib.auth import get_user_model
from TiendaApp.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.


Usuario = get_user_model()

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ["id"]
        
    @property
    def Total(self):
        return self.lineapedido_set.aggregate(
            total = Sum(
                F("Precio")*F("Cantidad"), output_field=FloatField()
            )
        )["total"]
        
    
    def __str__(self):
        return self.id

class LineaPedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id =  models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.Nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']
