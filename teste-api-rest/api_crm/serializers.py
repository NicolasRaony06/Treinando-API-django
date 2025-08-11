from rest_framework import serializers
from .models import Produto
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'