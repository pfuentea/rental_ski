from django.shortcuts import render, redirect
from .forms import RegistroForm 
from django.contrib.auth import login, authenticate

# Create your views here.


def index(request):
    return render(request, 'index.html')

def profile(request):




    return render(request, 'profile.html')


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