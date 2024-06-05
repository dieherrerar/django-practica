from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'index.html', {'usuario': request.user})

def registro(request):
    try:
        if request.method == "POST":
            usuario = request.POST.get('usuario')
            correo = request.POST.get('correo')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            print(usuario,correo,password1,password2)
            if password1==password2:
                user = User.objects.create_user(username=usuario, email=correo, password=password1)
                user.save()
                return render(request, 'login.html', {'mensaje': 'Usuario creado correctamente'})
            else:
                return render(request, 'registro.html',{'mensaje': 'Las contraseñas no coinciden'})
        elif request.method=='GET':
            return render(request, 'registro.html')

    except IntegrityError:
        return render(request,'registro.html',{'mensaje':'Usuario ya existe'})
    except Exception as error:
        print(error)


def iniciar_sesion(request):
    try:
        if request.method == "POST":
            usuario = request.POST.get('usuario')
            password = request.POST.get('password')
            user = authenticate(request, username=usuario, password=password)
            login(request, user)
            return render(request, 'index.html')
        elif request.method == 'GET':
            return render(request, 'login.html')
    except Exception as error:
        print(error)
