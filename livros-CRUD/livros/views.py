from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .models import livros
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    home = {'home': 'this is the home'}
    return JsonResponse(home)

def obter_livros(request):
    return JsonResponse(livros, safe=False)

def obter_livro_id(request, id):
    if request.method == 'GET':
        for livro in livros:
            if livro.get('id') == id:
                return JsonResponse(livro)
        
        return JsonResponse({'erro': 'id invalido'})
    
    return JsonResponse({'erro': 'metodo invalido'})

@csrf_exempt  
def criar_livro(request):
    if request.method == 'GET':
        return redirect(obter_livros)

    if request.method == 'POST':
        requisicao_post = request.body.decode('utf-8')
        requisicao_json = json.loads(requisicao_post)

        livros.append(requisicao_json)

        return JsonResponse(livros, safe=False)
    
    return JsonResponse({'erro': 'metodo invalido'})

@csrf_exempt  
def editar_livro(request, id):
    if request.method == 'GET':
        return JsonResponse(livros[id])

    if request.method == 'PUT':
        requisicao_put = request.body.decode('utf-8')
        requisicao_json = json.loads(requisicao_put)

        for indice, livro in enumerate(livros):
            if livro.get('id') == id:
                livros[indice].update(requisicao_json)
                return JsonResponse(livros[indice])

        return JsonResponse({'erro': 'id invalido'})
    
    return JsonResponse({'erro': 'metodo invalido'})

@csrf_exempt
def excluir_livro(request, id):
    if request.method == 'GET':
        return JsonResponse(livros[id])
    
    if request.method == 'DELETE':
        for indice, livro in enumerate(livros):
            if livro.get('id') == id:
                del livros[indice]
            
        return JsonResponse(livros, safe=False)
    
    return JsonResponse({'erro': 'metodo invalido'})

    
