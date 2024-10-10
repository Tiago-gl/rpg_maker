from django.urls import path
from . import views

urlpatterns = [
    path('sessao/criar/', views.criar_sessao, name='criar_sessao'),
    path('loja/<int:loja_id>/', views.ver_loja, name='ver_loja'),
    path('ficha/criar/', views.criar_ficha, name='criar_ficha'),
    path('comprar/<int:item_id>/', views.comprar_item, name='comprar_item'),
    # Outras URLs que você precisar
]
