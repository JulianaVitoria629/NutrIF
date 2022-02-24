from django.urls import path
from .views import  HomeView, RegisterUserView
from .views import FuncionarioCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('cadastro_de_usuario', RegisterUserView.as_view(), name='cadastro_de_usuario'),
    path('cadastrar/funcionario/', FuncionarioCreateView.as_view(), name='cadastrar-funcionario'),
]   