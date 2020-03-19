from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def Home(request):
    return render(request, 'micuenta/dashboard.html')


def Recibo(request):
    return render(request, 'micuenta/recibo.html')


def Usuario_Registro(request):
    return render(request, 'usuario_registro.html')


def Empleo_Registro(request):
    return render(request, 'empleo_registro.html')


def Empresa_Registro(request):
    return render(request, 'empresa_registro.html')
