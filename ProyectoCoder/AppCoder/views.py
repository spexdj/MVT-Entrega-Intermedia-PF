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
    return render(request,"AppCoder/buscarCurso.html")

def buscar(request):
    if request.get['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request,'AppCoder/resultadoCurso.html',{"camada":camada, "cursos":cursos})
    else:
        respuesta = "No enviaste Datos"
    return HttpResponse(respuesta)

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

##buscarPosts##

def buscarpost(request):
    return render(request,"AppCoder/busquedaPost.html")

def buscar2(request):
    post_views = request.GET['post_nombre']
    post_todos = Post.objects.filter(post_nombre__contains=post_views)
    return render(request,'AppCoder/resultadoPost.html',{"post_nombre":post_views, "posts": post_todos})


##buscarCategorias##

def buscarCategoria(request):
    return render(request,"AppCoder/busquedaCategoria.html")

def buscar3(request):
    categoria_views = request.GET['categoria_nombre']
    categoria_todos = Categoria.objects.filter(categoria_nombre__contains=categoria_views)
    return render(request,'AppCoder/resultadoCategoria.html',{"categoria_nombre":categoria_views, "categorias": categoria_todos})

##buscarUsuarios##

def buscarUsuario(request):
    return render(request,"AppCoder/busquedaUsuario.html")

def buscar4(request):
    usuario_views = request.GET['usuario_nombre']
    usuario_todos = Usuario.objects.filter(usuario_nombre__contains=usuario_views)
    return render(request,'AppCoder/resultadoUsuario.html',{"usuario_nombre":usuario_views, "usuarios": usuario_todos})

##CURSOS##

def leer_cursos(requerst):
    cursos_all = Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_all))

def crear_curso(request):
    curso = Curso(nombre='CursoTest',camada=199,numero_dia=19)
    curso.save()
    return HttpResponse(f'Curso {curso.nombre} ha sido creado')

def editar_curso(request):
    nombre_consulta = 'CursoTest'
    Curso.objects.filter(nombre=nombre_consulta).update(nombre='NombrenuevoCursoTest')
    return HttpResponse(f'Curso {nombre_consulta} ha sido actualizado')


def eliminar_curso(request):
    nombre_nuevo='NombrenuevoCursoTest'
    curso = Curso.objects.get(nombre=nombre_nuevo)
    curso.delete()
    return HttpResponse(f'Curso {nombre_nuevo} ha sido eliminado')


##POSTS##

def leer_posts(requerst):
    posts_all = Post.objects.all()
    return HttpResponse(serializers.serialize('json',posts_all))

def crear_post(request):
    post = Post(post_nombre='PostTest',post_totalcaracteres=199,post_puntaje=19)
    post.save()
    return HttpResponse(f'Post {post.post_nombre} ha sido creado')

def editar_post(request):
    nombre_consulta_post = 'PostTest'
    Post.objects.filter(post_nombre=nombre_consulta_post).update(post_nombre='NombrenuevoPostTest')
    return HttpResponse(f'Post {nombre_consulta_post} ha sido actualizado')


def eliminar_post(request):
    nombre_nuevo_post='NombrenuevoPostTest'
    post = Post.objects.get(post_nombre=nombre_nuevo_post)
    post.delete()
    return HttpResponse(f'Post {nombre_nuevo_post} ha sido eliminado')

##CATEGORIA##

def leer_categoria(requerst):
    categorias_all = Categoria.objects.all()
    return HttpResponse(serializers.serialize('json',categorias_all))

def crear_categoria(request):
    categoria = Categoria(categoria_nombre='CategoriaTest',categoria_importancia=199,categoria_descripcion='Esta es la categoria de CategoriaTest')
    categoria.save()
    return HttpResponse(f'Categoria {categoria.categoria_nombre} ha sido creada')

def editar_categoria(request):
    nombre_consulta_categoria = 'CategoriaTest'
    Categoria.objects.filter(categoria_nombre=nombre_consulta_categoria).update(categoria_nombre='NombrenuevoCategoriaTest')
    return HttpResponse(f'Categoria {nombre_consulta_categoria} ha sido actualizada')


def eliminar_categoria(request):
    nombre_nuevo_categoria='NombrenuevoCategoriaTest'
    categoria = Categoria.objects.get(categoria_nombre=nombre_nuevo_categoria)
    categoria.delete()
    return HttpResponse(f'Categoria {nombre_nuevo_categoria} ha sido eliminada')

##USUARIOS##

def leer_usuarios(requerst):
    usuarios_all = Usuario.objects.all()
    return HttpResponse(serializers.serialize('json',usuarios_all))

def crear_usuario(request):
    usuario = Usuario(usuario_nombre='UsuarioTest',usuario_apellido='UsuarioTest2',usuario_mail='maildeusuariotest2@mailfalso.com')
    usuario.save()
    return HttpResponse(f'Usuario {usuario.usuario_nombre} ha sido creado')

def editar_usuario(request):
    nombre_consulta_usuario = 'UsuarioTest'
    Usuario.objects.filter(usuario_nombre=nombre_consulta_usuario).update(usuario_nombre='NombrenuevoUsuarioTest')
    return HttpResponse(f'Usuario {nombre_consulta_usuario} ha sido actualizado')


def eliminar_usuario(request):
    nombre_nuevo_usuario='NombrenuevoUsuarioTest'
    usuario = Usuario.objects.get(usuario_nombre=nombre_nuevo_usuario)
    usuario.delete()
    return HttpResponse(f'Usuario {nombre_nuevo_usuario} ha sido eliminado')



###################################
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView

class CursoList(ListView):
    model = Curso
    template = 'AppCoder/curso_list.html'
class CursoCreate(CreateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/curso/list'
class CursoEdit(UpdateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/curso/list'
class CursoDetail(DetailView):
    model = Curso
    template = 'AppCoder/curso_detail.html'
class CursoDelete(DeleteView):
    model = Curso
    success_url = '/AppCoder/curso/list'

class PostList(ListView):
    model = Post
    template = 'AppCoder/post_list.html'
class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/AppCoder/post/list'
class PostEdit(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/AppCoder/post/list'
class PostDetail(DetailView):
    model = Post
    template = 'AppCoder/post_detail.html'
class PostDelete(DeleteView):
    model = Post
    success_url = '/AppCoder/post/list'

class CategoriaList(ListView):
    model = Categoria
    template = 'AppCoder/categoria_list.html'
class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppCoder/categoria/list'
class CategoriaEdit(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppCoder/categoria/list'
class CategoriaDetail(DetailView):
    model = Categoria
    template = 'AppCoder/categoria_detail.html'
class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = '/AppCoder/categoria/list'


class UsuarioList(ListView):
    model = Usuario
    template = 'AppCoder/usuario_list.html'
class UsuarioCreate(CreateView):
    model = Usuario
    fields = '__all__'
    success_url = '/AppCoder/usuario/list'
class UsuarioEdit(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = '/AppCoder/usuario/list'
class UsuarioDetail(DetailView):
    model = Usuario
    template = 'AppCoder/usuario_detail.html'
class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = '/AppCoder/usuario/list'        