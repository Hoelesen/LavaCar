from django import forms
  
# import GeeksModel from models.py
from .models import Cliente, Servico, TipoServico, Veiculo
  
# create a ModelForm
class TipoServicoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = TipoServico
        fields = "__all__"
  
# create a ModelForm
class ClienteForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Cliente
        fields = "__all__"
  
# create a ModelForm
class VeiculoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Veiculo
        fields = "__all__"
    
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), to_field_name="id", empty_label="Selecione")
  
# create a ModelForm
class ServicoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Servico
        fields = "__all__"
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.all(), to_field_name="id", empty_label="Selecione")
    data_entrada = forms.CharField(widget=forms.DateInput)
    data_saida = forms.CharField(widget=forms.DateInput)
    # itens = forms.MultiValueField()
  
    
