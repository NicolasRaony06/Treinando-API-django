import requests

link = "http://127.0.0.1:8000/api/produtos/"

def produtos_get_method():
    request = requests.get(
        url=link,
        headers=
        {'Authorization': f'Bearer'}
    )

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
    request = requests.post(
        url=link2,
        json={
            "produtos_id": [1],
            "quantidade": [2],
        },
        headers={
            'Authorization': f'Bearer'
        }
    )

    print(request.status_code)

#comprar_post_method()

link3 = "http://127.0.0.1:8000/api/usuarios/"

def usuarios_post_method():
    request = requests.post(url=link3, json={
        "username": "raony",
        "email": "raony@gmail.com",
        "password": "raony12345"
        }   
        )

    print(request.status_code)

#usuarios_post_method()

link = "http://127.0.0.1:8000/api/usuarios/login/"

def login_post_method():
    request = requests.post(url=link, json={
        "username": "raony",
        "password": "raony12345"
        }   
        )

    token = request.json()['access']
    refresh_token = request.json()['refresh']

    print(request.status_code)
    print(request.json())

    return token, refresh_token

token = login_post_method()[0]
token_refresh = login_post_method()[1]

link = "http://127.0.0.1:8000/api/usuarios/refresh/"

def refreshtoken_post_method():
    request = requests.post(url=link, json={
        "refresh": token_refresh,
        }   
        )

    print(request.status_code)
    print(request.json())

#refreshtoken_post_method()

link = "http://127.0.0.1:8000/api/dashboard/produtos/"

def dashboardprodutos_get_method():
    request = requests.get(
        url=link,
        headers={
            'Authorization': f'Bearer {token}'
        }
        )

    print(request.status_code)
    print(request.json())

#dashboardprodutos_get_method()

link = "http://127.0.0.1:8000/api/dashboard/faturamento/"

def dashboardfaturamento_get_method():
    request = requests.get(
        url=link,
        headers={
            'Authorization': f'Bearer {token}'
        }
        )

    print(request.status_code)
    print(request.json())

dashboardfaturamento_get_method()