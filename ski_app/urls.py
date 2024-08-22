from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'), 
    path('profile/', views.profile, name='profile'), # clientes pueden ver los equipo disponibles
    path('register/', views.register, name='register'),
    # /arriendos (get) , los operarios pueden ver los arriendos
    # /arriendos  (post) , agregar comentario al arriendo
    # /equipos/<id>/arrendar  (get), ruta para arrendar un equipo
    # /equipos/<id>/arrendar  (post) , confirma el arrendamiento


]