from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('user/<str:nickname>', views.get_user_by_nickname, name='get_user_by_nickname')
]