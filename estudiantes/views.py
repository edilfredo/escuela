from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm


# Create your views here.
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/registrar.html', {'form': form})