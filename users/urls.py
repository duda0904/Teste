from django.urls import path, include
from .views import create_user, user_edit, listar, detail, excluir, login_view

urlpatterns = [
    path('', listar, name="list-user"),
    path('create/', create_user, name="create-user"),
    path('detail/', detail , name="list-unique-user"),
    path('edit/', user_edit , name="edit-user"),
    path('delete/', excluir , name="delete-user"),
    path('login/', login_view, name="login_view" )

]