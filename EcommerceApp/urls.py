# URLS de la aplicacion, desde el proyecto se apunta a este archivo



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from EcommerceApp import views


#Ordeno las URLs de la aplicacion

urlpatterns = [
    path('', views.home, name="Home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 