from .views import get_users
from django.urls import path

urlpatterns = [
    path('get_users/', get_users, name='get_users')
]
