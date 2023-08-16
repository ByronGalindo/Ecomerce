from django.contrib import admin
from .models import CategoriaProdcuto, Producto

# Register your models here.

class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields =("Creada", "Actualizada")
    list_display= ("Nombre", "Creada", "Actualizada")
    search_fields = ("Nombre",)


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields =("Creado", "Actualizado")
    list_display= ("Nombre", "Precio", "Disponibilidad", "Creado", "Actualizado")
    list_filter= ("Precio", "Disponibilidad", "Creado", "Actualizado")
    search_fields = ("Nombre",)

admin.site.register(CategoriaProdcuto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)

