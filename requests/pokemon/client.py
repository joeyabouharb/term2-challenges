

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
        if r.status_code == 200:
            self.pokemon = r.json()['results']
        else:
            self.pokemon = []


    def get_pokemon(self):
        pass


if __name__ == '__main__':
    c = Client()
    c.pokemon
