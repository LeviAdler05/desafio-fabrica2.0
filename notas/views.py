from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota
from .forms import NotaForm

# Função para listar todas as notas
def listar_notas(request):
    # Obtém todas as instâncias do modelo Nota
    notas = Nota.objects.all()
    # Renderiza o template 'listar_notas.html' e passa a lista de notas como contexto
    return render(request, 'notas/listar_notas.html', {'notas': notas})

# Função para adicionar uma nova nota
def adicionar_nota(request):
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Cria um formulário NotaForm com os dados POST recebidos
        form = NotaForm(request.POST)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva a nova nota no banco de dados
            form.save()
            # Redireciona para a página de lista de notas após salvar
            return redirect('listar_notas')
    else:
        # Cria um formulário vazio se o método não for POST
        form = NotaForm()
    # Renderiza o template 'adicionar_nota.html' e passa o formulário como contexto
    return render(request, 'notas/adicionar_nota.html', {'form': form})

# Função para atualizar uma nota existente
def atualizar_nota(request, pk):
    # Obtém a nota com o identificador pk ou retorna um erro 404 se não encontrada
    nota = get_object_or_404(Nota, pk=pk)
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Cria um formulário NotaForm com os dados POST recebidos e a instância da nota
        form = NotaForm(request.POST, instance=nota)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva as alterações no banco de dados
            form.save()
            # Redireciona para a página de lista de notas após salvar
            return redirect('listar_notas')
    else:
        # Cria um formulário com os dados da nota existente se o método não for POST
        form = NotaForm(instance=nota)
    # Renderiza o template 'atualizar_nota.html' e passa o formulário como contexto
    return render(request, 'notas/atualizar_nota.html', {'form': form})

# Função para remover uma nota existente
def remover_nota(request, pk):
    # Obtém a nota com o identificador pk ou retorna um erro 404 se não encontrada
    nota = get_object_or_404(Nota, pk=pk)
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Exclui a nota do banco de dados
        nota.delete()
        # Redireciona para a página de lista de notas após a exclusão
        return redirect('listar_notas')
    # Renderiza o template 'remover_nota.html' e passa a nota como contexto
    return render(request, 'notas/remover_nota.html', {'nota': nota})

