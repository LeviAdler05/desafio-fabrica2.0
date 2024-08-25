from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    # Define a classe NotaForm
    class Meta:
        # Especifica as configurações do formulário para o modelo Nota.
        model = Nota  # Define o modelo associado a este formulário como Nota.
        fields = ['titulo', 'conteudo']  # Diz quais campos do modelo Nota devem ser incluídos no formulário.

