import json
from flask import Flask, jsonify,  abort, request
from flask.wrappers import Response

from database.db import *
from controller import *

with db_session:
    if Filme.select().first() is None:
        populate_database()


app = Flask(__name__)


@app.route('/movies', methods=['GET'])
def get_all_movies():
    resp = jsonify({'movies': json.loads(all_movies())})
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')

    return resp


@app.route('/movies/<int:idMovie>', methods=['GET'])
def detail_movie(idMovie):
    resp = jsonify(json.loads(detail_movies(idMovie)))
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')

    return resp


@app.route('/movies', methods=['POST'])
def add_movie():
    if not request.json or not 'nome' in request.json:
        abort(400)

    movie = add_movies(request.json['nome'],
                       request.json['ano'], request.json['genero'])

    resp = jsonify(json.loads(movie))
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')

    return resp, 201


@app.route('/movies/<int:idMovie>', methods=['PUT'])
def put_movie(idMovie):
    check_movie = jsonify(json.loads(detail_movies(idMovie)))
    print(len(check_movie.data) == 41)
    if (len(check_movie.data) == 41):
        movie = add_movies(request.json['nome'],
                           request.json['ano'], request.json['genero'])
        resp = jsonify(json.loads(movie))

    else:
        movie = update_movie(idMovie, request.json['nome'],
                             request.json['ano'], request.json['genero'])
        resp = jsonify(json.loads(movie))

    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')

    return resp, 201


@app.route('/movies/<int:idMovie>', methods=['PATCH'])
def patch_movie(idMovie):
    movie = patch_movies(idMovie, request.json['nome'])
    resp = jsonify(json.loads(movie))

    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Authorization:', 'Basic YWxhZGRpbjpvcGVuc2VzYW1l')

    return resp, 201


@app.route('/movies/<int:idMovie>', methods=['DELETE'])
def delete_movie(idMovie):
    resp = remove_movie(idMovie)
    if (not resp):
        abort(404)

    return jsonify(json.loads(resp)), 200


@app.route('/movies', methods=['OPTIONS'])
def options_movie():
    return {}


@app.route('/movies', methods=['HEAD'])
def head():
    resp = Response()

    return resp


if __name__ == '__main__':
    print('Servidor no ar!')
    app.run(host='0.0.0.0', debug=True)
