from django.shortcuts import render

from ServiciosApp.models import servicio


# Create your views here.


def servicios(request):
    
    Servicios = servicio.objects.all        #Importo todos los servicios registrados como servicios
    
    return render(request, 'ServiciosApp/servicios.html', {'Servicios':Servicios})
