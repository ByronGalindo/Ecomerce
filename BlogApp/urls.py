# URLS de la aplicacion, desde el proyecto se apunta a este archivo



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


#Ordeno las URLs de la aplicacion

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categorias_id>/',views.categoria, name="Categoria"),
]
