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
    # Serviços
    path('novo-servico/', views.novo_servico, name='novo_servico'),
    path('servicos-efetuar/', views.servicos_efetuar, name='servicos_efetuar'),

]