from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProdutoSerializer
from .models import Produto

@api_view(['GET', 'POST', 'PUT'])
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "PUT":
        try:
            produto_id = request.data["id"]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            produto_to_change = Produto.objects.get(id=produto_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProdutoSerializer(produto_to_change, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)



