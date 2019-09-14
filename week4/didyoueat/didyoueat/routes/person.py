"""
person routes
"""
from didyoueat.server import app
from didyoueat.read_write import get_lunches


@app.route('/person/<name>', methods=['GET'])
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
