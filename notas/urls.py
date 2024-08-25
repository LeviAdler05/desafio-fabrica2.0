from django.urls import path
from . import views

# lista de padrões de URL para o aplicativo.
urlpatterns = [
    # padrão de URL para a página inicial do aplicativo.
    # Quando a URL for '', chama a função listar_notas da views e a nomeia como 'listar_notas'.
    path('', views.listar_notas, name='listar_notas'),
    
    # Define o padrão de URL para a página de adicionar uma nova nota.
    # Quando a URL for 'adicionar/', chama a função adicionar_nota da views e a nomeia como 'adicionar_nota'.
    path('adicionar/', views.adicionar_nota, name='adicionar_nota'),
    
    # Define o padrão de URL para a página de atualizar uma nota existente.

    # Quando a URL corresponder a esse padrão, chama a função atualizar_nota da views e a nomeia como 'atualizar_nota'.
    path('atualizar/<int:pk>/', views.atualizar_nota, name='atualizar_nota'),
    
    # Define o padrão de URL para a página de remover uma nota existente.
    # Quando a URL corresponder a esse padrão, chama a função remover_nota da views e a nomeia como 'remover_nota'.
    path('remover/<int:pk>/', views.remover_nota, name='remover_nota'),
]
