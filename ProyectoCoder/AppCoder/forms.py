from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    numero_dia = forms.IntegerField()

######################################
######################################

class Postformulario(forms.Form):
    post_nombre = forms.CharField()
    post_totalcaracteres = forms.IntegerField()
    post_puntaje = forms.IntegerField()


class Usuarioformulario(forms.Form):
    usuario_nombre = forms.CharField()
    usuario_apellido = forms.CharField()
    usuario_mail = forms.CharField()  


class Categoriaformulario(forms.Form):
    categoria_nombre = forms.CharField()
    categoria_importancia = forms.IntegerField()
    categoria_descripcion = forms.CharField() 