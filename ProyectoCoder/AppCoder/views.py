from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.models import Post
from AppCoder.models import Usuario
from AppCoder.models import Categoria
from django.core import serializers
from AppCoder.forms import CursoFormulario
from AppCoder.forms import Postformulario
from AppCoder.forms import Usuarioformulario
from AppCoder.forms import Categoriaformulario

# Create your views here.
def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    if request.method == "POST":
        
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                # informacion = {'curso':'1223','numero_dia:1}
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"], numero_dia=informacion["numero_dia"])
                curso.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
                
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def profesores(request):
    return HttpResponse('Vista de profesores')

def cursosapi(request):
    cursos_todos = Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos))

###vista de busqueda con form###
def buscarcurso(request):
    return render(request,"AppCoder/busquedaCurso.html")

def buscar(request):
    camada_views = request.GET['camada']
    curso_todos = Curso.objects.filter(camada=camada_views)
    return render(request,'AppCoder/resultadoCurso.html',{"camada":camada_views, "cursos": curso_todos})

###################################
###################################
def post(request):
    if request.method == "POST":
        
            miFormulario2 = Postformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario2)
            
            if miFormulario2.is_valid:
                informacion2 = miFormulario2.cleaned_data
                # informacion = {'curso':'1223','numero_dia:1}
                post = Post(post_nombre=informacion2["post_nombre"], post_totalcaracteres=informacion2["post_totalcaracteres"], post_puntaje=informacion2["post_puntaje"])
                post.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario2 = Postformulario()
                
    return render(request, "AppCoder/post.html", {"miFormulario2": miFormulario2})

def postapi(request):
    post_todos = Post.objects.all()
    return HttpResponse(serializers.serialize('json',post_todos))

def usuario(request):
    if request.method == "POST":
        
            miFormulario3 = Usuarioformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario3)
            
            if miFormulario3.is_valid:
                informacion3 = miFormulario3.cleaned_data
                # informacion = {'curso':'1223','numero_dia:1}
                usuario = Usuario(usuario_nombre=informacion3["usuario_nombre"], usuario_apellido=informacion3["usuario_apellido"], usuario_mail=informacion3["usuario_mail"])
                usuario.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario3 = Usuarioformulario()
                
    return render(request, "AppCoder/usuario.html", {"miFormulario3": miFormulario3})

def usuarioapi(request):
    usuario_todos = Usuario.objects.all()
    return HttpResponse(serializers.serialize('json',usuario_todos))

def categoria(request):
    if request.method == "POST":
        
            miFormulario4 = Categoriaformulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario4)
            
            if miFormulario4.is_valid:
                informacion4 = miFormulario4.cleaned_data
                # informacion = {'curso':'1223','numero_dia:1}
                categoria = Categoria(categoria_nombre=informacion4["categoria_nombre"], categoria_importancia=informacion4["categoria_importancia"], categoria_descripcion=informacion4["categoria_descripcion"])
                categoria.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario4 = Categoriaformulario()
                
    return render(request, "AppCoder/categoria.html", {"miFormulario4": miFormulario4})   

def categoriaapi(request):
    categoria_todos = Categoria.objects.all()
    return HttpResponse(serializers.serialize('json',categoria_todos))



def buscarpost(request):
    return render(request,"AppCoder/busquedaPost.html")

def buscar2(request):
    post_views = request.GET['post_nombre']
    post_todos = Post.objects.filter(post_nombre=post_views)
    return render(request,'AppCoder/resultadoPost.html',{"post_nombre":post_views, "posts": post_todos})