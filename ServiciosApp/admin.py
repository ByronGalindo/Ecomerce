from django.contrib import admin

from .models import servicio

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields =("FechaCreacionServicio", "FechaActualizacionServicio")
    list_display = ("NombreServicio", "ContenidoServicio", "FechaCreacionServicio", "FechaActualizacionServicio")
    list_filter = ( "FechaCreacionServicio", "FechaActualizacionServicio",)
    search_fields = ("NombreServicio",)
    date_hierarchy = "FechaActualizacionServicio"
    
    

admin.site.register(servicio, ServiciosAdmin)