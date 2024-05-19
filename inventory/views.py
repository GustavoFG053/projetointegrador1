from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Products
from .forms import ProductsForm

def index(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro")
    else:
        form = ProductsForm()

    return render(request, "index.html", {"form": form, "titulo": "Adicionar nova coleta"})

def registro(request):
    produtos = Products.objects.all()
    context = {"produtos": produtos}
    return render(request, "registro.html", context)

def confirmar_troca(request, produto_id):
    produto = get_object_or_404(Products, id=produto_id)
    produto.troca_confirmada = True
    produto.save()
    return redirect("registro")

def recusar_troca(request, produto_id):
    produto = get_object_or_404(Products, id=produto_id)
    produto.troca_confirmada = False
    produto.save()
    return redirect("registro")

def excluir_registro(request, produto_id):
    produto = get_object_or_404(Products, id=produto_id)
    produto.delete()
    return redirect("registro")

def editar_produto(request, produto_id):
    produto = get_object_or_404(Products, pk=produto_id)
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProductsForm(instance=produto)

    return render(request, "editar_produto.html", {"form": form, "produto": produto})

def sobre(request):
    return render(request, "sobre.html")

@user_passes_test(lambda u: u.is_superuser)
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

@user_passes_test(lambda u: u.is_superuser)
def excluir_usuarios(request):
    if request.method == 'POST':
        usuarios_a_excluir = request.POST.getlist('usuarios_a_excluir')
        for usuario_id in usuarios_a_excluir:
            try:
                usuario = User.objects.get(pk=usuario_id)
                usuario.delete()
            except User.DoesNotExist:
                pass  # Se o usuário não existe, apenas continue para o próximo
        
        # Remover todas as mensagens existentes
        storage = messages.get_messages(request)
        for message in storage:
            pass  # Ignorar todas as mensagens existentes
        
        # Adicionar a mensagem de sucesso de exclusão
        messages.success(request, 'Usuário(s) excluído(s) com sucesso!')
        return redirect('pagina_de_confirmacao')  # Redireciona para a página de confirmação

    return redirect('pagina_de_erro')  # Se a solicitação não for POST, redireciona para a página de erro

def pagina_de_confirmacao(request):
    return render(request, 'pagina_de_confirmacao.html')

def pagina_de_erro(request):
    return render(request, 'pagina_de_erro.html')

