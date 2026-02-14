from django.shortcuts import render
from . import models


def index(request):
    datos = {
        "titulo": "python",
        "descripcion": "Frame work para crear aplicaciones web",
    }
    return render(request, "prueba/index.html", datos)


def notas(request):
    mis_notas = [10, 9, 8, 7, 6, 5]
    return render(request, "prueba/notas.html", {"notas": mis_notas})


def clientes_list(request):
    clientes = models.Cliente.objects.all()
    return render(render, "prueba/clientes.html", context={"clientes": clientes})
