from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def formulario(request):
    if request.method == "POST":

        codigo = request.POST.get("codigo")
        prensa = request.POST.get("prensa")
        pesador1 = request.POST.get("pesador1")
        pesador2 = request.POST.get("pesador2")

        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        RUTA_ARCHIVO = r"C:\Users\User\Desktop\proyecto\produccion.txt"

        with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{fecha_creacion} | "
                f"Código: {codigo} | "
                f"Prensa: {prensa} | "
                f"P1: {pesador1} | "
                f"P2: {pesador2}\n"
            )

        return HttpResponse("Datos guardados correctamente")

    return render(request, "formulario.html")