import requests

link = 'http://127.0.0.1:8000/totalvendas/'
requisicao = requests.get(link).json()
total_vendas = requisicao['total_vendas']
print(f'O total das vendas é R$ {total_vendas:.2f}')

