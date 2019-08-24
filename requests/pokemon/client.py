

import requests

class Client():
    """
    client service to interact with the api
    """
    _URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        self._setup()

    def _setup(self):
        r = requests.get(
            f'{self._URL}/pokemon'
        )
        self.pokemon = r.json()['results']


    def get_pokemon(self):
        pass

if __name__ == '__main__':
    c = Client()
    c.pokemon
