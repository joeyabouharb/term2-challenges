"""
class demo by joseph abouharb
"""

class Person:
    """
    create a person
    """
    def __init__(
            self: object,
            first_name: str,
            last_name: str
    ):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        """
        greeting message
        """
        print(f'Hello, my name is {self.first_name} {self.last_name}')

    def set_first_name(
            self: object,
            first_name: str
    ):
        """
        changes first name
        """
        self.first_name = first_name

FELICIA = Person(
    'Felicia',
    'Smith'
)
FELICIA.greet()

GREG = Person(
    'Greg',
    'Smith'
)
GREG.greet()
GREG.set_first_name('joey')
GREG.greet()
