import requests
import time
import os


base_url = 'http://localhost:5000/movies'


def get_all_movies():
    response = requests.get(base_url)

    return response.json()


def get_detail_movie(id_movie):
    response = requests.get(f'{base_url}/{id_movie}')

    return response.json()


def post_new_movie(movie):
    response = requests.post(base_url, json=movie)

    return response.json()


def delete_movie(id_movie):
    response = requests.delete(f'{base_url}/{id_movie}')

    return response.json()


action = 1
while action != 0:
    time.sleep(1)

    print('Qual metodo vc que usar? ')
    print(
        'Opcoes:\n[0] Para sair\n[1] Listar todos os filmes\n[2] Listar um filme\n[3] Adicionar novo filme\n[4] Deletar filme')
    action = int(input())

    if action == 0:
        break
    elif action == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(get_all_movies())
    elif action == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Digite o id do filme:')
        movie_id = int(input('ID: '))

        print(get_detail_movie(movie_id))
    elif action == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Digite as informações do filme: ')
        nome = str(input('Nome: '))
        ano = int(input('Ano: '))
        genero = str(input('Genero: '))

        movie = {
            "nome": nome,
            "ano": ano,
            "genero": genero
        }

        print(post_new_movie(movie=movie))
    elif action == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Digite o id do filme para deletar:')
        movie_id = int(input('ID: '))

        print(delete_movie(movie_id))
