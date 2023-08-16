from django.contrib import admin
from .models import categorias, post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    
    readonly_fields =("FechaCreacionCategoria", "FechaActualizacionCategoria")
    list_display = ("NombreCategoria", "FechaCreacionCategoria", "FechaActualizacionCategoria")
    search_fields = ("NombreCategoria",)
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields =("FechaCreacionPost", "FechaActualizacionPost")
    list_display = ("NombrePost", "ContenidoPost", "FechaCreacionPost", "FechaActualizacionPost")
    list_filter = ( "FechaCreacionPost", "FechaActualizacionPost","AutorPost")
    search_fields = ("NombrePost",)



admin.site.register(categorias, CategoriaAdmin)
admin.site.register(post, PostAdmin)

