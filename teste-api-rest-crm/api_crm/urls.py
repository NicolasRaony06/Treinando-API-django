from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('produtos/', views.produtos_api, name="produtos_api"),
    path('comprar_produtos/', views.comprar_produtos, name="comprar_produtos"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('usuarios/login/', TokenObtainPairView.as_view(), name="obter_token_login"),
    path('usuarios/refresh/', TokenRefreshView.as_view(), name="refresh_token_login"),
    path('dashboard/produtos/', views.dashboard_produtos, name="dashboard_produtos"),
    path('dashboard/faturamento/', views.dashboard_faturamento, name="dashboard_faturamento"),
]
