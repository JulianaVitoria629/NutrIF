from django.urls import path
from .views import  HomeView, RegisterUserView
from .views import FuncionarioCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('cadastro_de_usuario', RegisterUserView.as_view(), name='cadastro_de_usuario'),



    path('validar_cadastro_usuario', FuncionarioCreateView.as_view(), name='validar_cadastro_usuario'),
]   