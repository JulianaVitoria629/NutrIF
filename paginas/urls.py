from django.urls import path
from .views import HomeView, RegisterUserView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cadastro_de_usuario', RegisterUserView.as_view(), name='cadastro_de_usuario'),
]