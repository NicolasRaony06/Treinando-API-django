import requests

link = "http://127.0.0.1:8000/api/produtos/"

def produtos_get_method():
    request = requests.get(url=link)

    print(request.json())
    print(request.status_code)

#produtos_get_method()

def produtos_put_method():
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

def produtos_delete_method():
    request = requests.delete(url=link, json={
        "id": 2
        }   
        )

    print(request.status_code)

#produtos_delete_method()


link2 = "http://127.0.0.1:8000/api/comprar_produtos/"

def comprar_post_method():
    request = requests.post(url=link2, json={
        "produtos_id": [1],
        "quantidade": [2],
        }   
        )

    print(request.status_code)

comprar_post_method()




