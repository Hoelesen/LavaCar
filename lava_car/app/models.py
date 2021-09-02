from django.db import models
from enum import IntEnum

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
    cpf_ou_cnpj = models.CharField(max_length=14)
    nome_fantasia = models.CharField(max_length=60)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
    
class Veiculo(models.Model):
    tipo_veiculo = models.IntegerField(choices=TipoVeiculo.choices(), default=TipoVeiculo.CARRO)
    placa = models.CharField(max_length=7)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50)
    
class TipoServico(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60)
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    forma_pagamento = models.IntegerField(choices=FormaPagamento.choices())
    tipo_veiculo = models.IntegerField(choices=TipoVeiculo.choices(), default=TipoVeiculo.CARRO)

class ServicoItem(models.Model):
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.RESTRICT)

class Servico(models.Model):
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    numero_nota = models.CharField(max_length=60)
    codigo_verificacao = models.CharField(max_length=60)
    desconto = models.DecimalField(decimal_places=2, max_digits=4)
    status = models.IntegerField(choices=ServicoStatus.choices(), default=ServicoStatus.AGUARDANDO_LAVAGEM)
    itens = models.ManyToManyField(ServicoItem)

