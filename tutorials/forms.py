from django import forms
from tutorials.models import Tutorial, AvaliacaoTutorial
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class TutorialForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tutorial
        fields = ('titulo', 'conteudo','aplicacao')

class AvaliacaoTutorialForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoTutorial
        fields = ('avaliacao', 'text')