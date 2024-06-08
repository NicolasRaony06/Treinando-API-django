from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_user_by_nickname(request, nickname):
    try:
        user = User.objects.get(pk=nickname)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(user, request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    if request.method == 'GET':  
        try:                                                           #Tenta com a url /?user=algumvalor
            if request.GET['user']:                                  #Checar se request.GET['user'] não está recebendo um valor None
                nickname = request.GET['user']
 
                try:
                    user = User.objects.get(pk=nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:                                                      #Caso request.GET['user'] receba None, retorna um erro http 400
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:                                                        #Caso a url seja passada com um parâmetro errado, retorna http 400
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':

        novo_user = request.data
        print(request.data)

        serializer = UserSerializer(data=novo_user)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)    

    if request.method == 'PUT':
        try:
            nickname = request.data['nickname']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            changed_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(changed_user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
