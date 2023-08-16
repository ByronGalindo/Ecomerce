# URLS de la aplicacion, desde el proyecto se apunta a este archivo



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


#Ordeno las URLs de la aplicacion

app_name = "CarroApp" 
urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="Agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="Eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="Restar"),
    path("limpiar/", views.limpiar_carro, name="Limpiar"),

]