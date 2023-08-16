from django.shortcuts import render, HttpResponse, redirect
from .forms import FormularioContacto
from  django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def contacto(request):
    Formulario_Contacto = FormularioContacto()
    if request.method =="POST":
        Formulario_Contacto = FormularioContacto(data= request.POST)
        if Formulario_Contacto.is_valid():
            Nombre= request.POST.get("Nombre")
            Email= request.POST.get("Email")
            Contenido= request.POST.get("Contenido")
            CorreSalida = EmailMessage(
                "Comunicación desde App Django",
                "El usuario {} te escribe desde la dirección {} : \n\n {}".format(Nombre,Email,Contenido),
                "",
                ["djangodevapps@gmail.com"],
                reply_to=[Email]
            )
            try:
                CorreSalida.send()
                return redirect("/contacto/?check")
            except:
                return redirect("/contacto/?failed")
    else:
        Formulario_Contacto = FormularioContacto()    
    return render(request, 'ContactoApp/contacto.html', {'Formulario': Formulario_Contacto})




# def contacto(request):
    
#     if request.method == "POST":   #-> Verificacion de la confirmacion del envio de datos
        
#         Formilario = FormularioContacto(request.POST)
        
#         if Formilario.is_valid():   # El formulario supera la validacion, es valido
#             informacion = Formilario.cleaned_data   # Recupero la informacion del formulario
#             send_mail(
#                 informacion['asunto'],
#                 informacion['mensaje'],
#                 informacion.get('email',''),
#                 ['aquimelomandas@gmail.com'],
#                 )
#             return render(request,'Confirmacion.html')
#     else:         
#         Formilario = FormularioContacto()
        
#     return render(request,'FormularioContacto.html', {'form': Formilario})