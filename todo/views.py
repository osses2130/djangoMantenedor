from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareasForm

# Create your views here.
def home(request):
    tareas = Tarea.objects.all()
    context = {"tareas": tareas}
    return render(request, "todo/home.html",context)

def agregar(request):
    if request.method=="POST":
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareasForm()

    context = {"form" : form}
    return render(request, 'todo/agregar.html', context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id = tarea_id)
    tarea.delete()
    return redirect("home")


def editar(request, tarea_id):
    tarea = Tarea.objects.get(id = tarea_id)
    if request.method == "POST":
        form = TareasForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareasForm(instance = tarea)

    context = {"form": form }
    return render(request, 'todo/editar.html', context)