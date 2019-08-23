"""
an app that does something
"""
from os import system


def delete_item(user_list: dict) -> None:
    view_list(user_list)
    selected = input('To Delete: ')
    if user_list.get(selected, False):
        del user_list[selected]


def view_list(user_list: dict) -> None:
    checked_item = lambda item: (
        f'{item}: {user_list[item]}' 
    )
    print("\n".join(
        checked_item(item)
        for item in user_list.keys())
    )


def add_to_list(shopping_list: list, user_list: dict):
    """
    add to list
    """
    list_to_string = "\n".join(
        f'{index+1}) {item}'
        for index, item
        in enumerate(shopping_list)
    )
    print(list_to_string)
    is_valid = False
    while not is_valid:
        selected = input(
        'select item/s to add to your shopping list, seperated with a " " '
        ).split(' ')
        is_all_decimal = lambda data: all(num.isdecimal() for num in data)
        if is_all_decimal(selected):
            is_valid = validate_user_input(selected, shopping_list)
        if not is_valid:
            input('select again! ')
    for value in is_valid:
        key = shopping_list[value-1]
        user_list.update({
            key: user_list.get(key, 0) + 1
        })


def validate_user_input(selected: list, shopping_list: list) -> int:
    """
    validates user input
    """
    try:
        indexes = [int(num) for num in selected]
    except ValueError:
        exit('woops')
    if not all(
        len(shopping_list) >= i > 0
        for i in indexes
    ):
        return False
    return indexes


def app_menu(shopping_list, user_list):
    menu = {
        'add': add_to_list,
        'delete': delete_item,
        'view': view_list,
        'exit': exit
    }
    system('clear')
    option = menu.get(input('add, delete, view or exit? '), None)

    if option is None:
        return None
    elif option == view_list or option == delete_item:
        option(user_list)
    elif  option == exit:
        option()
    else:
        option(shopping_list, user_list)
    input('Press Enter to continue...')


def main():
    """
    
    """
    shopping_list = [
        'tomato', 'bread',
        'cabbage', 'tuna',
        'salmon', 'Apple',
        'mayonnaise', 'chocolate',
        'biscuit', 'peanut butter'
        ]
    user_dict = dict()

    while True:
        app_menu(shopping_list, user_dict)


if __name__ == '__main__':
    main()
    
