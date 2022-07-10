from django.urls import path, include
from .views import (listar, 
                create_tutorials, 
                detail, 
                tutorials_edit, 
                excluir,
                create_avaliacao,
                avaliacao_edit,
                excluir_avaliacao
                )

urlpatterns = [
    path('', listar, name="list-tutorials"),
    path('create/', create_tutorials, name="create-tutorials"),
    path('detail/<int:tutorials_id>/', detail, name="list-unique-tutorials"),
    path('edit/<int:tutorials_id>/', tutorials_edit, name="edit-tutorials"),
    path('delete/<int:tutorials_id>/', excluir, name="delete-tutorials"),

    path('detail/<int:tutorials_id>/avaliacao-create/', create_avaliacao, name="create-avaliacao"),
    path('detail/<int:tutorials_id>/avaliacao-edit/', avaliacao_edit, name="edit-avaliacao"),
    path('detail/<int:tutorials_id>/avaliacao-delete/', excluir_avaliacao, name="delete-avaliacao"),

]