import requests

def alterar_livro():
    link = 'http://127.0.0.1:8000/livros/editar/4'

    requests.put(url=link, json=
        {
            'id': 4,
            'titulo': 'No pain No gain',
            'autor': 'Kinzim Somebody',
        }
    )

#alterar_livro()

def deletar_livro():
    link = 'http://127.0.0.1:8000/livros/excluir/4'

    requests.delete(link)

#deletar_livro()

def criar_livro():
    link = 'http://127.0.0.1:8000/livros/criar'

    requests.post(link, json=
        {
            'id': 5,
            'titulo': 'No pain No gain',
            'autor': 'Kinzim Somebody',
        }
    )

#criar_livro()