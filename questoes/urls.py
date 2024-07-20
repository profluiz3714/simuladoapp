from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questao/adicionar/', views.adicionar_questao, name='adicionar_questao'),
    path('questao/editar/<int:id>/', views.editar_questao, name='editar_questao'),
    path('questao/excluir/<int:id>/', views.excluir_questao, name='excluir_questao'),
    path('gerar_simulado/', views.gerar_simulado, name='gerar_simulado'),
    path('gerar_planilha/', views.gerar_planilha, name='gerar_planilha'),
    path('recomecar/', views.recomecar, name='recomecar'),
    path('registro/', views.registro, name='registro'),
    path('listar_questoes/', views.listar_questoes, name='listar_questoes'),
]
