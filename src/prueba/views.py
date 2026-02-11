from django.shortcuts import render


def index(request):
    datos = {
        "titulo": "Django",
        "descripcin": "framework para crear aplicaciones web",
    }
    return render(request, "prueba/index.html", datos)
