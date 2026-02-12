from django.shortcuts import render


def index(request):
    datos = {
        "titulo": "python",
        "descripcion": "Frame work para crear aplicaciones web",
    }
    return render(request, "prueba/index.html", datos)


def notas(request):
    mis_notas = [10, 9, 8, 7, 6, 5]
    return render(request, "prueba/notas.html", {"notas": mis_notas})
