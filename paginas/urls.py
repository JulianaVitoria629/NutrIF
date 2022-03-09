from django.urls import path
from .views import  HomeView, RegisterUserView
from .views import FuncionarioCreateView, LoginUserView, RegisterAlimentoView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login_de_usuario', LoginUserView.as_view(), 
    name='login_de_usuario'),

    path('registro_de_alimento', RegisterAlimentoView.as_view(), name='registro_de_alimento'),
    
    path('cadastro_de_usuario', RegisterUserView.as_view(), name='cadastro_de_usuario'),
    
    path ('registro', RegisterView.as_view(), 
    name= 'registro'),
    
    path('cadastrarfuncionario/', FuncionarioCreateView.as_view(), name='cadastrarfuncionario/'),
    
    ]