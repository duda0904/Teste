from django import forms
from aplicacao.models import AplicacaoTutorial


class AplicacaoTutorialForm(forms.ModelForm):
    class Meta:
        model = AplicacaoTutorial
        fields = ('nome', 'funcionalidade')