"""
validates form data for lunch entry
"""

from didyoueat.read_write import get_lunches


def is_valid_form(
        name: str, lunch: str
):
    """
    takes in the entered name and lunch details
    ensures they do not exist in the json file
    and returns a boolean if true
    """
    if not name or not lunch:
        return (
            False,
            'please enter valid inputs for name and lunch'
        )
    data = get_lunches() 
    for data in data['data']:
        if data['name'] == name:
            return (
                False,
                'Name already exists!'
            )
    else:
        return (
            True,
            'Added lunch details.'
        )
