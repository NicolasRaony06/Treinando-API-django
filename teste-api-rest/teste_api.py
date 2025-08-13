import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1MDA1MTI2LCJpYXQiOjE3NTUwMDQ4MjYsImp0aSI6Ijk2YWIyYzIwOGI0NTQ0ZDc4YzYwMDVhMWIxNjU5NTY3IiwidXNlcl9pZCI6IjUifQ.cBn38IG4TWJ6LiFMeksWoSflZxAuewHvUKBe3RNPX0s"

token_refresh = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NTA5MDc4OCwiaWF0IjoxNzU1MDA0Mzg4LCJqdGkiOiIyMzQ2ZTlhZTk2YTM0MzkzYWM4M2Y0ODg5OTg0OWEzYyIsInVzZXJfaWQiOiI1In0.Mpf0ltrKTNyZR9ARiViEf7m_s3N6-xIWIWRjSzAAwiM'

link = "http://127.0.0.1:8000/api/produtos/"

def produtos_get_method():
    request = requests.get(
        url=link,
        headers=
        {'Authorization': f'Bearer {token}'}
    )

    print(request.json())
    print(request.status_code)

produtos_get_method()

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
            'Authorization': f'Bearer {token}'
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

link4 = "http://127.0.0.1:8000/api/usuarios/login/"

def login_post_method():
    request = requests.post(url=link4, json={
        "username": "raony",
        "password": "raony12345"
        }   
        )

    print(request.status_code)
    print(request.json())

#login_post_method()

link5 = "http://127.0.0.1:8000/api/usuarios/refresh/"

def refreshtoken_post_method():
    request = requests.post(url=link5, json={
        "refresh": token_refresh,
        }   
        )

    print(request.status_code)
    print(request.json())

#refreshtoken_post_method()

link5 = "http://127.0.0.1:8000/api/dashboard/produtos/"

def dashboardprodutos_get_method():
    request = requests.post(url=link5, json={
        "refresh": token_refresh,
        }   
        )

    print(request.status_code)
    print(request.json())

