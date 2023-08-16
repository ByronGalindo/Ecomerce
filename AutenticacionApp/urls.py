# URLS de la aplicacion, desde el proyecto se apunta a este archivo



from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Register, log_out, log_in


#Ordeno las URLs de la aplicacion

app_name= "AutenticacionApp"
urlpatterns = [
    path('', Register.as_view(), name="Register"),
    path('log_out/', log_out, name="Logout"),
    path('log_in/', log_in, name="Login"),
]
