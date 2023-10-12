"""
URL configuration for entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Appentrega import views
from .views import (saludo, inicio, pag1, pag2, pag3, 
                              cursoFormulario, buscarCurso)


urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('saludo/', views.saludo, name="saludo"),
    path('curso/', views.curso, name="curso"),
    path('pag1/', views.pag1, name="pag1"),
    path('pag2/', views.pag2, name="pag2"),
    path('pag3/', views.pag3, name="pag3"),
    path('F/', cursoFormulario, name="Cursoformulario"),
    path('buscarCurso/', buscarCurso, name="BuscarCurso"),
   
]
