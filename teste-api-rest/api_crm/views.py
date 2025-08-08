from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProdutoSerializer
from .models import Produto

@api_view(['GET', 'POST'])
def produtos_api(request):
    if request.method == "GET":
        produtos = Produto.objects.all()

        serializer = ProdutoSerializer(produtos, many=True).data

        return Response(serializer)
    
    if request.method == "POST":
        novo_produto = request.data

        serializer = ProdutoSerializer(data=novo_produto)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
