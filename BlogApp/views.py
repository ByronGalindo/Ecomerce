from django.shortcuts import render
from BlogApp.models import post, categorias
# Create your views here.


def blog(request):
    
    Posts = post.objects.all()
    return render(request, 'BlogApp/blog.html',{'Posts':Posts})

def categoria(request, categorias_id):
    
    Categoria = categorias.objects.get(id= categorias_id)
    Posts = post.objects.filter(Categorias=Categoria)
    return render(request,'BlogApp/categorias.html', {'Categoria':Categoria, 'Posts':Posts})