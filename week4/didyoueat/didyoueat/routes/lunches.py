"""
lunches routes
"""

from flask import request, Blueprint
from werkzeug.exceptions import HTTPException
from didyoueat.read_write import get_lunches, update_lunches
from didyoueat.validators import is_valid_form

lunch_routes = Blueprint('lunch_routes', __name__, url_prefix='/lunches')


@lunch_routes.route('', methods=['GET'])
def get_all_lunches():
    """
    gets all the lunches
    """
    data = get_lunches()
    return data


@lunch_routes.route('', methods=['post'])
def post_lunch():
    """
    add new lunch entry
    """
    name = request.json.get(
        'name', False
    ).capitalize()
    lunch = request.json.get(
        'lunch', False
    ).capitalize()
    is_valid, message = is_valid_form(
        name, lunch
    )
    if not is_valid:
        return message
    lunches = get_lunches()
    lunches['data'].lunch_routesend({
        'name': name,
        "lunch": lunch
    })
    update_lunches(lunches)
    return message


@lunch_routes.route('/<name>', methods=['DELETE'])
def delete_person(name: str):
    """
    delete a person by name
    """
    lunches = get_lunches()
    for data in lunches['data']:
        if data['name'] == name.capitalize():
            break
    else:
        return 'Not Found'
    return f'Successfully deleted {name}'


@lunch_routes.route('/<meal>')
def get_persons_who_ate(meal: str):
    """
    get all person's who ate a specific meal
    returns them as dict if they exist
    """
    result = {
        "results": []
    }
    lunches = get_lunches()
    for data in lunches['data']:
        if data['lunch'] == meal.capitalize():
            result['results'].append(data)
    return result \
        if result['results']\
        else 'Not found'
