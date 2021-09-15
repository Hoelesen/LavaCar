from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # Aqui criamos as rotas chamando cada view
    path('novo-servico/', views.novo_servico, name='novo_servico'),
]