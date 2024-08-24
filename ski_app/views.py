from django.shortcuts import render, redirect
from .forms import RegistroForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Equipo, Estado,Arriendo,Usuario


def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    if request.user.is_authenticated:
        user=Usuario.objects.get(id=request.user.id)   
        if user.id_tipo_user.tipo_user == 'operario':
            return redirect('arriendos')
    equipos= Equipo.objects.filter(estado__nombre='disponible')
    context={
        'equipos':equipos
    }

    return render(request, 'profile.html',context=context)


def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = RegistroForm()

    context = {
        'form' : form,
    }
    return render(request, 'registration/register.html', context)

@login_required
def arrendar(request,id):
    equipo = Equipo.objects.get(id=id)
    if request.method=='POST':
        equipo.estado=Estado.objects.get(nombre='arrendado')
        equipo.save()
        cliente = Usuario.objects.get(id=request.user.id)
        Arriendo.objects.create(cliente=cliente, equipo=equipo,fecha=request.POST['fecha'])
        return redirect('profile')

    context = {
        'equipo':equipo
    }
    return render(request, 'arrendar.html', context)

@login_required
def arriendos(request):
    #equipos= Equipo.objects.filter(estado__nombre='arrendado')
    arriendos=Arriendo.objects.filter(equipo__estado__nombre='arrendado')
    context={
        'arriendos':arriendos
    }

    return render(request, 'arriendos.html',context=context)

@login_required
def add_comentario(request,arriendo_id):
    arriendo=Arriendo.objects.get(id=arriendo_id)
    arriendo.observacion=request.POST['comentario']
    arriendo.save()
    return redirect('arriendos')