from django import forms
from .models import Sessao, FichaJogador, Races

class SessaoForm(forms.ModelForm):
    class Meta:
        model = Sessao
        fields = ['nome', 'descricao']

class FichaJogadorForm(forms.ModelForm):
    class Meta:
        model = FichaJogador
        fields = ['nome_personagem', 'sessao', 'imagem_base']
        model = Races
        fields = ['nome']
