from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/listar_notas.html', {'notas': notas})

def adicionar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/adicionar_nota.html', {'form': form})

def atualizar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('listar_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/atualizar_nota.html', {'form': form})

def remover_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('listar_notas')
    return render(request, 'notas/remover_nota.html', {'nota': nota})


# Create your views here.
