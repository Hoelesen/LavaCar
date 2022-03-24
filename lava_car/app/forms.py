from django import forms

# Personalizando input datetime
class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    # Set DATETIME_INPUT_FORMATS here because, if USE_L10N 
    # is True, the locale-dictated format will be applied 
    # instead of settings.DATETIME_INPUT_FORMATS.
    # See also: 
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Date_and_time_formats
     
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")
  
# import GeeksModel from models.py
from .models import Acerto, Cliente, Funcionario, Servico, TipoServico, Veiculo
  
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
    data_entrada = DateTimeLocalField()
    data_saida = DateTimeLocalField()
    itens = forms.ModelMultipleChoiceField(
        queryset=TipoServico.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class AcertoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Acerto
        fields = "__all__"
    servico = forms.ModelChoiceField(queryset=Servico.objects.all(), to_field_name="id", empty_label="Selecione", widget=forms.HiddenInput())
    funcionario = forms.ModelChoiceField(queryset=Funcionario.objects.all(), to_field_name="id", empty_label="Selecione")
    observacao = forms.Textarea()
  
    
