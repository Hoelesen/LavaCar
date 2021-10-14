from django.contrib import admin
from .models import Cliente,TipoServico,Servico,ServicoItem,Veiculo

admin.site.register(Cliente)
admin.site.register(TipoServico)
admin.site.register(Servico)
admin.site.register(ServicoItem)
admin.site.register(Veiculo)
