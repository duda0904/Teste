from django.contrib import admin

# Register your models here.
from .models import Tutorial, AplicacaoTutorial

admin.site.register(Tutorial)
admin.site.register(AplicacaoTutorial)
