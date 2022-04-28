from django.shortcuts import render

# Create your views here.

def inicio (req):

    return render (req, 'AppAJ/inicio.html')

def trabajos_realizados (req):

    return render (req, 'AppAJ/trabajos_realizados.html')

def materiales (req):

    return render (req, 'AppAJ/materiales.html')

def nosotros (req):

    return render (req, 'AppAJ/nosotros.html')

def contacto (req):

    return render (req, 'AppAJ/contacto.html')

def acerca_de_mi (req):
    return render (req, 'AppAJ/acerca_de_mi.html')