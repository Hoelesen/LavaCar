from django.contrib import admin
from .models import Cliente, Funcionario, TipoServico, Servico, Veiculo

admin.site.register(Cliente)
admin.site.register(TipoServico)
admin.site.register(Servico)
admin.site.register(Veiculo)
admin.site.register(Funcionario)
