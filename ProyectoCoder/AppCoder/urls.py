from django.urls import path
from AppCoder import views


urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path('cursos/', views.cursos,name='Cursos'),
    path('cursosApi/', views.cursosapi),
    path('profesores/', views.profesores),
    path('busquedaCurso/', views.buscarcurso),
    path('buscar/', views.buscar),
    ############################################
    path('post/', views.post,name='Post'),
    path('postApi/', views.postapi),
    path('usuario/', views.usuario,name='Usuario'),
    path('usuarioApi/', views.usuarioapi),
    path('categoria/', views.categoria,name='Categoria'),
    path('categoriaApi/', views.categoriaapi),
    path('buscar2/', views.buscar2),
    path('busquedaPost/', views.buscarpost),    
]