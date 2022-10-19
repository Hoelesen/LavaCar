from django.conf.urls import include
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # Aqui criamos as rotas chamando cada view
    # Login
    path('login/', views.login, name='login'),
    # Contas de usuário
    path('accounts/', include('django.contrib.auth.urls')),
    # Tipos de serviço
    path('tipos-servico/create/', views.tipo_servico_create, name='tipo_servico_create'),
    path('tipos-servico/edit/<id>', views.tipo_servico_edit, name='tipo_servico_edit'),
    path('tipos-servico/delete/<id>', views.tipo_servico_delete, name='tipo_servico_delete'),
    path('tipos-servico/', views.tipo_servico_list, name='tipo_servico_list'),
    # Clientes
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('clientes/edit/<id>', views.cliente_edit, name='cliente_edit'),
    path('clientes/delete/<id>', views.cliente_delete, name='cliente_delete'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    # Veículos
    path('veiculos/create/', views.veiculo_create, name='veiculo_create'),
    path('veiculos/edit/<id>', views.veiculo_edit, name='veiculo_edit'),
    path('veiculos/delete/<id>', views.veiculo_delete, name='veiculo_delete'),
    path('veiculos/', views.veiculo_list, name='veiculo_list'),
    # Serviços
    path('servicos/create/', views.servico_create, name='servico_create'),
    path('servicos/edit/<id>', views.servico_edit, name='servico_edit'),
    path('servicos/delete/<id>', views.servico_delete, name='servico_delete'),
    path('servicos/', views.servico_list, name='servico_list'),
    #  Financeiro
    path('financeiro/', views.financeiro_list, name='financeiro_list'),
    # Acertos
    path('servicos/<servico_id>/acertos/create/', views.acerto_create, name='acerto_create')
]