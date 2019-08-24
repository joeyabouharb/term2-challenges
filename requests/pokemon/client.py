

import requests
import json


MAX_POKEMON = 964
class Client():
    """
    client service to interact with the api
    """
    _URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        pass

    def get_pokemon(self, limit=20, offset=0):
        params = f'?limit={limit}&offset={offset}'
        r = requests.get(
            f'{self._URL}/pokemon/{params}'
        )
        if r.status_code == 200:
            self.pokemon = json.dumps(r.json()['results'], indent=2)
        else:
            print('Connection Error. ')

    def find_by_id(self, id):
        r = requests.get(
            f'{self._URL}/pokemon/{id}'
        )
        if r.status_code == 200:
            self.pokemon = json.dumps(r.json(), indent=4)
        else:
            exit('connection error')
    
    def find_by_name(self, name):
        r = requests.get(
            f'{self._URL}/pokemon/{name}'
        )
        if r.status_code == 200:
            self.pokemon = json.dumps(r.json(), indent=4)
        elif r.status_code == 404:
            exit('pokemon not found')
        else:
            exit('connection error!')
if __name__ == '__main__':
    c = Client()
    c.pokemon
