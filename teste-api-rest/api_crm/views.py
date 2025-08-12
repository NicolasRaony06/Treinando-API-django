from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProdutoSerializer, UsuarioSerializer
from .models import Produto, Venda, ItemVenda

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
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
    
    if request.method == 'DELETE':
        try:
            produto_id = request.data["id"]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            produto = Produto.objects.get(id=produto_id)
            produto.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comprar_produtos(request):
    if request.method == 'POST':
        try:
            produtos_id = request.data["produtos_id"]
            quantidade = request.data["quantidade"]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if produtos_id:
            valor_total = 0
            for index, produto_id in enumerate(produtos_id):
                try:
                    produto = Produto.objects.get(id=produto_id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                if produto.ativo:
                    try: 
                        qtd_produto = quantidade[index]
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    
                    venda = Venda.objects.create()

                    item = ItemVenda.objects.create(
                        venda = venda,
                        produto = produto,
                        qtd_produto=qtd_produto,
                        preco_und=produto.preco
                    )

                    if qtd_produto <= produto.qtd_estoque:
                        produto.qtd_estoque -= qtd_produto
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    
                    if produto.qtd_estoque < 1:
                        produto.ativo = False

                    try:
                        produto.save()
                        valor_total += item.subtotal()
                        item.save()
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST)

            try:     
                venda.valor_total = valor_total
                venda.save()
                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def usuarios(request):
    if not request.data:
        return Response({"erro": "Nenhum dado enviado"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



