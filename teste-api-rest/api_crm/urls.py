from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos_api, name="produtos_api"),
    path('comprar_produtos/', views.comprar_produtos, name="comprar_produtos"),
    path('usuarios/', views.usuarios, name="usuarios"),
]
