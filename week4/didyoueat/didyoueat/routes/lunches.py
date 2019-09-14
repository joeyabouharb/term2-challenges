"""
lunches routes
"""

from flask import request
from werkzeug.exceptions import HTTPException
from didyoueat.read_write import get_lunches, update_lunches
from didyoueat.server import app
from didyoueat.validators import is_valid_form


@app.route('/lunches/', methods=['GET'])
def get_all_lunches():
    """
    gets all the lunches
    """
    data = get_lunches()
    return data


@app.route('/lunches', methods=['post'])
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
    lunches['data'].append({
        'name': name,
        "lunch": lunch
    })
    update_lunches(lunches)
    return message


@app.route('/lunches/<name>', methods=['DELETE'])
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


@app.route('/lunches/<meal>')
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
    return \
        result if result['results']\
        else 'Not found'
