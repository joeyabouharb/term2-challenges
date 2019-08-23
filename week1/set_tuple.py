"""
print values seperated by commas into a tuple list
"""

def main(user_input: str) -> None:
    """
    entrypoint
    """
    list_data = user_input.split(', ')
    is_list_valid = all(n.isdecimal() for n in list_data)
    if is_list_valid:
        try:
            number_list = [int(n) for n in list_data]
        except ValueError:
            raise ValueError('Bad Input! ')
        print(tuple(number_list))


if __name__ == '__main__':
    print(
        'Welcome! this application prints a list of numbers taken as input. '
        'Please input data seperated with commas. eg "2, 4"'
        )
    main(input('input list data: '))
    