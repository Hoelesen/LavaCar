from django import forms
  
# import GeeksModel from models.py
from .models import TipoServico
  
# create a ModelForm
class TipoServicoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = TipoServico
        fields = "__all__"