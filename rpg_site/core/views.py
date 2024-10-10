from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sessao, Mestre, Loja, Item, FichaJogador
from .forms import SessaoForm, FichaJogadorForm

#MESTRE
@login_required
def criar_sessao(request):
    # Verifica se o usuário é um mestre
    if hasattr(request.user, 'mestre'):
        if request.method == 'POST':
            form = SessaoForm(request.POST)
            if form.is_valid():
                sessao = form.save(commit=False)
                sessao.mestre = request.user.mestre  # Atribui o mestre atual
                sessao.save()
                return redirect('sessao_detalhes', sessao_id=sessao.id)
        else:
            form = SessaoForm()
        return render(request, 'criar_sessao.html', {'form': form})
    else:
        return redirect('home')  # Se não for mestre, redireciona para a home

#FICHAS - PERSONAGENS
@login_required
def criar_ficha(request):
    if request.method == 'POST':
        form = FichaJogadorForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.jogador = request.user
            ficha.save()
            return redirect('ficha_detalhes', ficha_id=ficha.id)
    else:
        form = FichaJogadorForm()
    
    return render(request, 'criar_ficha.html', {'form': form})

# LOJAS - ITEMS
@login_required
def ver_loja(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id)
    itens = Item.objects.filter(loja=loja)

    return render(request, 'ver_loja.html', {'loja': loja, 'itens': itens})

@login_required
def comprar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    ficha = FichaJogador.objects.get(jogador=request.user)

    # Verifica se o jogador já tem esse item
    if item not in ficha.itens.all():
        ficha.itens.add(item)
        # Você pode adicionar lógica para reduzir o saldo do jogador se necessário
        ficha.save()

    return redirect('ver_loja', loja_id=item.loja.id)