from django.urls import path, include
from .views import create_aplicacao, aplicacao_edit, excluir_aplicacao


urlpatterns = [
    path('create/', create_aplicacao, name="create-aplicacao"),
    path('edit/<int:tutorials_id>/', aplicacao_edit, name="edit-aplicacao"),
    path('delete/<int:tutorials_id>/', excluir_aplicacao, name="delete-aplicacao"),

]