from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
class Register(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'AutenticacionApp/register.html', {'form': form})
        
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for error in form.error_messages:
                messages.error(request, form.error_messages[error])
            return render(request, 'AutenticacionApp/register.html', {'form': form})
        
def log_out(request):
    logout(request)
    return redirect('Home')


def log_in(request):
    
    if request.method == "POST":
        form =  AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario =  form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            Usuario = authenticate(username=usuario, password=contrasena)
            if Usuario is not None:
                login(request, Usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario inválido!")
        else:
            messages.error(request, "Información inválida!")
    form =  AuthenticationForm()
    return render(request, 'AutenticacionApp/login.html', {'form': form})

