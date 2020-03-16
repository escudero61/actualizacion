from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('usuario_registro/', views.Usuario_Registro),
    path('empleo_registro/', views.Empleo_Registro),
    path('empresa_registro/', views.Empresa_Registro)
]
