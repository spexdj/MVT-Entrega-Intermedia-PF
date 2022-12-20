from django.urls import path
from AppCoder import views


urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path('cursos/', views.cursos,name='Cursos'),
    path('cursosApi/', views.cursosapi),
    path('profesores/', views.profesores),
    path('buscarCurso/', views.buscarcurso,name='Buscar'),
    path('buscar/', views.buscar),
    ############################################
    path('post/', views.post,name='Post'),
    path('postApi/', views.postapi),
    path('usuario/', views.usuario,name='Usuario'),
    path('usuarioApi/', views.usuarioapi),
    path('categoria/', views.categoria,name='Categoria'),
    path('categoriaApi/', views.categoriaapi),
    #################BUSQUEDAS##################
    path('buscar2/', views.buscar2,name='BusquedaPost'),
    path('busquedaPost/', views.buscarpost),
    path('busquedaCategoria/', views.buscarCategoria),
    path('buscar3/', views.buscar3,name='BusquedaCategoria'),
    path('busquedaUsuario/', views.buscarUsuario), 
    path('buscar4/', views.buscar4,name='BusquedaUsuario'),
    #################CRUDS##################
    path('leerCursos/', views.leer_cursos),
    path('crearcurso/', views.crear_curso),
    path('editarcurso/', views.editar_curso),
    path('eliminarcurso/', views.eliminar_curso),

    path('leerposts/', views.leer_posts),
    path('crearpost/', views.crear_post),
    path('editarpost/', views.editar_post),
    path('eliminarpost/', views.eliminar_post),

    path('leercategoria/', views.leer_categoria),
    path('crearcategoria/', views.crear_categoria),
    path('editarcategoria/', views.editar_categoria),
    path('eliminarcategoria/', views.eliminar_categoria),

    path('leerusuarios/', views.leer_usuarios),
    path('crearusuario/', views.crear_usuario),
    path('editarusuario/', views.editar_usuario),
    path('eliminarusuario/', views.eliminar_usuario),    

###############CRUD########################
    path('curso/list/', views.CursoList.as_view(),name='List'),
    path('post/list/', views.PostList.as_view(),name='Listpost'),
    path('categoria/list/', views.CategoriaList.as_view(),name='Listcategoria'),
    path('usuario/list/', views.UsuarioList.as_view(),name='Listusuario'),

    path('curso/create/', views.CursoCreate.as_view(),name='New'),
    path('categoria/create/', views.CategoriaCreate.as_view(),name='Newcategoria'),            
    path('usuario/create/', views.UsuarioCreate.as_view(),name='Newusuario'),            
    path('post/create/', views.PostCreate.as_view(),name='Newpost'),

    path('curso/edit/<pk>', views.CursoEdit.as_view(),name='Edit'),   
    path('categoria/edit/<pk>', views.CategoriaEdit.as_view(),name='Editcategoria'),            
    path('usuario/edit/<pk>', views.UsuarioEdit.as_view(),name='Editusuario'),           
    path('post/edit/<pk>', views.PostEdit.as_view(),name='Editpost'),

    path('curso/detail/<pk>', views.CursoDetail.as_view(),name='Detail'),   
    path('categoria/detail/<pk>', views.CategoriaDetail.as_view(),name='Detailcategoria'),            
    path('usuario/detail/<pk>', views.UsuarioDetail.as_view(),name='Detailusuario'),           
    path('post/detail/<pk>', views.PostDetail.as_view(),name='Detailpost'),

    path('curso/delete/<pk>', views.CursoDelete.as_view(),name='Delete'), 
    path('categoria/delete/<pk>', views.CategoriaDelete.as_view(),name='Deletecategoria'),            
    path('usuario/delete/<pk>', views.UsuarioDelete.as_view(),name='Deleteusuario'),           
    path('post/delete/<pk>', views.PostDelete.as_view(),name='Deletepost'),    
]