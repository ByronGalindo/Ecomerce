from django.contrib import admin

# Register your models here.

from .models import LineaPedido, Pedido


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)    
    list_display = ('usuario','creado')
    list_filter = ('usuario','creado')
    search_fields = ("usuario",)


class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)    
    list_display = ('usuario','producto_id', "cantidad")
    list_filter = ('usuario','creado','producto_id')
    search_fields = ("usuario", 'producto_id')



admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)
