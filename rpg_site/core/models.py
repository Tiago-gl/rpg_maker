from django.db import models
from django.contrib.auth.models import User

class tipo_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.TextField()

class Sessao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=1000)
    mestre = models.ForeignKey(User, on_delete=models.CASCADE)

class Loja(models.Model):
    nome = models.CharField(max_length=200)
    image_base = models.TextField(max_length=1000, null=True)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

class Atributos(models.Model):
    nome = models.TextField()
    valor = models.TextField()

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ataque = models.IntegerField(null=True)
    defesa = models.IntegerField(null=True)
    defesa_magica = models.IntegerField(null=True)
    image_base = models.TextField(max_length=1000, null=True)
    atributos = models.ForeignKey(Atributos, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

class Monstro(models.Model):
    nome = models.CharField(max_length=100)
    vida = models.IntegerField()
    ataque = models.IntegerField()
    defesa_fisica = models.IntegerField()
    defesa_magica = models.IntegerField()
    nivel = models.IntegerField()
    element = models.TextField()
    crit_rate = models.DecimalField()
    evasion = models.DecimalField()
    moviment = models.IntegerField()
    exp = models.IntegerField()
    gold = models.IntegerField()
    drop = models.TextField(max_length=1000)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

class AtaqueMonstro(models.Model):
    nome_ataque = models.TextField()
    tipo = models.TextField()
    dano = models.IntegerField()
    elemento = models.TextField()
    alcance = models.IntegerField()
    area = models.TextField()
    efeito_1 = models.TextField()
    efeito_2 = models.TextField()
    descricao = models.TextField()
    monster = models.ForeignKey(Monstro, on_delete=models.CASCADE)

class FichaJogador(models.Model):
    jogador = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_personagem = models.CharField(max_length=100)
    crit_rate = models.DecimalField()
    evasion = models.DecimalField()
    moviment = models.IntegerField()
    nivel = models.IntegerField(default=0)
    image_base = models.TextField(max_length=1000, null=True)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item, blank=True)

class Races(models.Model):
    nome = models.CharField(max_length=100)
    bonus_1 = models.TextField()
    bonus_2 = models.TextField()
    bonus_3 = models.TextField()
    bonus_4 = models.TextField()
    bonus_5 = models.TextField()
    bonus_6 = models.TextField()
    alcance = models.IntegerField()
    habilidade = models.TextField(max_length=1000)
    habilidade_2 = models.TextField(max_length=1000)
    desvantagem = models.TextField(max_length=1000)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
    
class profissao(models.Model):
    nome = models.CharField(max_length=100)
    bonus_1 = models.TextField()