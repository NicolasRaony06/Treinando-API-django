import requests

link = "http://127.0.0.1:8000/api/produtos/"

request = requests.put(url=link, json={
    "id": 2,
    "nome": "chocolate",
    "descricao": "chocolate chocolate chocolate",
    "preco": "6.90",
    "qtd_estoque": 59,
    "ativo": True
    }   
    )

print(request.status_code)

