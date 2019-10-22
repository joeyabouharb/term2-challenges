"""
"""


from math import ceil
from flask import (
    Flask, request, Response, render_template
)
from client import Client, PokemonCache
from services import stream
from services import generator

CACHE = PokemonCache()
CLIENT = Client(CACHE)
APP = Flask(__name__)


@APP.route('/<color>')
def get_color(color):
    """
    get all pokemon specified by color
    """
    CLIENT.find_by_name('pokemon-color', color)
    try:
        page = int(request.args.get('page', 1))
    except:
        return '<h1>404 Not Found.</h1>'
    if isinstance(CLIENT.result, int):
        return f'<h1>{CLIENT.result} Error</h1>'
    else:
        limit = ceil(
            len(CLIENT.result['pokemon_species']) / 15
        )
        if page > limit:
            page = 1
        return Response(stream.template(
            APP, 'color.html',
            result=generator.species_list(CLIENT, page),
            limit=limit, color=color
        ))

@APP.route('/')
def index():
    """
    root dir
    """
    CLIENT.get_all('pokemon-color')
    return Response( stream.template(
        APP, 'index.html',
        result=generator.all_pokemon_colors(CLIENT.result)
    ))


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=1234)
