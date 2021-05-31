import json
from flask import Flask, jsonify,  abort, make_response, request, url_for

from database.db import *
from controller import *

with db_session:
    if Filme.select().first() is None:
        populate_database()


app = Flask(__name__)


@app.route('/movies', methods=['GET'])
def get_all_movies():
    return jsonify({'movies': json.loads(all_movies())})


@app.route('/movies', methods=['POST'])
def add_movie():
    if not request.json or not 'nome' in request.json:
        abort(400)

    res = add_movies(request.json['nome'],
                     request.json['ano'], request.json['genero'])

    return jsonify(json.loads(res)), 201


@app.route('/movies/<int:idMovie>', methods=['GET'])
def detail_movie(idMovie):
    res = detail_movies(idMovie)

    return jsonify(json.loads(res))


@app.route('/movies/<int:idMovie>', methods=['DELETE'])
def delete_movie(idMovie):
    res = remove_movie(idMovie)

    return jsonify(json.loads(res))


if __name__ == '__main__':
    print('Servidor no ar!')
    app.run(host='0.0.0.0', debug=True)
