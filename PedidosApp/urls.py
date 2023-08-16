# URLS de la aplicacion, desde el proyecto se apunta a este archivo



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


#Ordeno las URLs de la aplicacion
app_name = "PedidosApp"
urlpatterns = [
    path('', views.procesar_pedido, name="ProcesarPedido"),
]