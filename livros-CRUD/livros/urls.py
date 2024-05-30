"""
URL configuration for livros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("livros/", obter_livros, name='obter_livros'),
    path("livros/<int:id>", obter_livro_id, name='obter_livro_id'),
    path("livros/criar", criar_livro, name='criar_livro'),
    path("livros/editar/<int:id>", editar_livro, name='editar_livro'),
    path("livros/excluir/<int:id>", excluir_livro, name='excluir_livro'),
]
