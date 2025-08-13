from rest_framework import serializers
from .models import Produto, ItemVenda
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoFaturamentoSerializer(serializers.ModelSerializer):
    faturamento = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'qtd_estoque', 'faturamento']

    def get_faturamento(self, obj):
        valor_total = 0
        for item in ItemVenda.objects.filter(produto=obj):
            valor_total += item.subtotal()
        return valor_total

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # não retorna a senha na resposta
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # criptografa a senha
        user.save()
        return user