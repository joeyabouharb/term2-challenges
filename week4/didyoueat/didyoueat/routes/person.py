"""
person routes
"""
from flask import Blueprint
from didyoueat.read_write import get_lunches

person_routes = Blueprint(
        'person_route', __name__, url_prefix='/person'
)

@person_route.route('/<name>', methods=['GET'])
def get_person_lunch(name: str):
    """
    get the person's lunch by name
    returns them in a dict/json
    """
    lunches = get_lunches()
    for element in lunches['data']:
        if name.capitalize() == element['name']:
            return element
    return 'not found.'
