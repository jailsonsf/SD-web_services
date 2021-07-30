import json
from database.db import *


@db_session
def all_movies():
    result = select(f for f in Filme)[:]

    movies = []
    for m in result:
        movie = {
            "id": m.id,
            "nome": m.nome,
            "ano_lancamento": m.ano_lancamento,
            "genero": m.genero
        }

        movies.append(movie)

    response = json.dumps(movies)

    return response


@db_session
def detail_movies(id):
    try:
        result = Filme.get(id=id)

        movie = {
            "id": result.id,
            "nome": result.nome,
            "ano_lancamento": result.ano_lancamento,
            "genero": result.genero
        }

        response = json.dumps(movie)
    except:
        response = json.dumps({'msg': 'Filme não encontrado'})

    return response


@db_session
def add_movies(nome, ano, genero):
    movie = Filme(nome=nome, ano_lancamento=ano, genero=genero)

    response = {
        'msg': 'Filme adicionado',
    }

    response = json.dumps(response)

    return response


@db_session
def update_movie(id, nome, ano, genero):
    try:
        result = Filme.get(id=id)

        if nome != '':
            result.nome = nome
        if ano != None:
            result.ano = ano
        if genero != '':
            result.genero = genero

        response = {
            'msg': 'Filme Atualizado',
        }

        response = json.dumps(response)

    except:
        response = {
            'msg': 'Filme não encontrado'
        }
        response = json.dumps(response)

    return response


@db_session
def patch_movies(id, nome):
    try:
        result = Filme.get(id=id)

        if nome != '':
            result.nome = nome

        response = {
            'msg': 'Filme Atualizado',
        }

        response = json.dumps(response)

    except:
        response = {
            'msg': 'Filme não encontrado'
        }
        response = json.dumps(response)

    return response


@db_session
def remove_movie(id):
    try:
        result = Filme.get(id=id)
        result.delete()

        response = {
            'msg': 'Filme deletado'
        }
    except:
        response = {
            'msg': 'Filme nao encontrado'
        }

    response = json.dumps(response)

    return response
