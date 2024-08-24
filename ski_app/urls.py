from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'), 
    path('profile/', views.profile, name='profile'), # clientes pueden ver los equipo disponibles
    path('register/', views.register, name='register'),
    # /arriendos (get) , los operarios pueden ver los arriendos
    path('arriendos/', views.arriendos, name='arriendos'),
    path('add_comentario/<int:arriendo_id>',views.add_comentario,name='add_comentario'),
    # /arriendos  (post) , agregar comentario al arriendo
    path('equipos/<int:id>/arrendar', views.arrendar, name='arrendar'),
    # /equipos/<id>/arrendar  (get), ruta para arrendar un equipo
    # /equipos/<id>/arrendar  (post) , confirma el arrendamiento


]