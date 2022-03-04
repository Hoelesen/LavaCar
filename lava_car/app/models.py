from datetime import datetime
from enum import IntEnum

from django.db import models

class TipoVeiculo(IntEnum):
  MOTO = 1
  CARRO = 2
  CAMINHONETE = 3
  CAMINHAO = 4
  ONIBUS = 5
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class FormaPagamento(IntEnum):
  AVISTA = 1
  APRAZO = 2
  CARTAO_CREDITO = 3
  CARTAO_DEBITO = 4
  PIX = 5
  GESTOR_FROTAS = 6
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class ServicoStatus(IntEnum):
  AGUARDANDO_LAVAGEM = 1
  LAVAGEM_ANDAMENTO = 2
  AGUARDANDO_LIMPEZA = 3
  LIMPEZA_ANDAMENTO = 4
  FINALIZADO = 5
  ENTREGUE = 6
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

# Create your models here.
class Cliente(models.Model):    
    nome = models.CharField(max_length=60)
    cpf_ou_cnpj = models.CharField(max_length=14, verbose_name="CPF/CNPJ")
    nome_fantasia = models.CharField(max_length=60, verbose_name="Nome fantasia")
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=60, verbose_name="E-mail")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    logradouro = models.CharField(max_length=60)
    numero = models.IntegerField(verbose_name="Número")
    complemento = models.CharField(max_length=60, blank=True, default='')
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self) -> str:
        return self.nome
    
class Veiculo(models.Model):
    tipo_veiculo = models.IntegerField(choices=TipoVeiculo.choices(), default=TipoVeiculo.CARRO, verbose_name="Tipo")
    placa = models.CharField(max_length=7)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, verbose_name="Descrição", blank=True, default='')

    def __str__(self) -> str:
        return self.placa
    
class TipoServico(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60, verbose_name="Descrição", blank=True, default='')
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    tipo_veiculo = models.IntegerField(choices=TipoVeiculo.choices(), default=TipoVeiculo.CARRO, verbose_name="Tipo")
    
    def __str__(self) -> str:
        return self.nome + ' - ' + str(self.valor) 

class Servico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.RESTRICT, verbose_name="Veículo")
    data_entrada = models.DateTimeField(verbose_name="Data/Hora entrada")
    data_saida = models.DateTimeField(verbose_name="Data/Hora saída")
    numero_nota = models.CharField(max_length=60, verbose_name="N° da nota", blank=True, default='')
    codigo_verificacao = models.CharField(max_length=60, verbose_name="Código de verificação", blank=True, default='')
    desconto = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="Desconto", default=0)
    forma_pagamento = models.IntegerField(choices=FormaPagamento.choices(), verbose_name="Forma de pagamento")
    status = models.IntegerField(choices=ServicoStatus.choices(), default=ServicoStatus.AGUARDANDO_LAVAGEM)
    observacao = models.CharField(max_length=60, verbose_name="Observação", blank=True, default='')
    itens = models.ManyToManyField(TipoServico, db_column="")

    def get_forma_pagamento_label(self):
      if self.forma_pagamento == FormaPagamento.APRAZO:
          return "À prazo"
      if self.forma_pagamento == FormaPagamento.AVISTA:
          return "À vista"
      if self.forma_pagamento == FormaPagamento.CARTAO_CREDITO:
          return "Cartão de crédito"
      if self.forma_pagamento == FormaPagamento.CARTAO_DEBITO:
          return "Cartão de débito"
      if self.forma_pagamento == FormaPagamento.GESTOR_FROTAS:
          return "Gestor de frotas"
      if self.forma_pagamento == FormaPagamento.PIX:
          return "PIX"

    def get_status_label(self):
      if self.status == ServicoStatus.AGUARDANDO_LAVAGEM:
          return "Aguardando lavagem"
      if self.status == ServicoStatus.AGUARDANDO_LIMPEZA:
          return "Aguardando limpeza"
      if self.status == ServicoStatus.LAVAGEM_ANDAMENTO:
          return "Lavagem em andamento"
      if self.status == ServicoStatus.LIMPEZA_ANDAMENTO:
          return "Limpeza em andamento"
      if self.status == ServicoStatus.ENTREGUE:
          return "Entregue"
      if self.status == ServicoStatus.FINALIZADO:
          return "Finalizado"
              

