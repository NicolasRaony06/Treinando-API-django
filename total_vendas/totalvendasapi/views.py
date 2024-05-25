from django.http import HttpResponse, JsonResponse
import pandas as pd

def home(request):
    return HttpResponse('API funcionando')

def totalvendas(request):
    dados = pd.read_csv('././base_dados.csv')
    total_vendas = dados['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    
    return JsonResponse(resposta)