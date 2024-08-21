from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),

    
]