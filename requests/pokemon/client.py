

import requests
import json

class SearchItem:

    def __init__(self, stats):
        for key in stats.keys():
            setattr(self, key, stats[key])

    def toString(self):
        out = ''
        search_dict = list(self.__dict__.keys())
        for key in search_dict:
            out += f'{key}: {self.__dict__[key]}\n'
        return out


class Client():
    """
    client service to interact with the api
    """
    _URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        pass

    def get_all(self, item, limit=20, offset=0):
        """
        return all pokemon
        """
        params = f'?limit={limit}&offset={offset}'
        r = requests.get(
            f'{self._URL}/{item}{params}'
        )
        if r.status_code == 200:
            self.result = json.dumps(r.json()['results'], indent=2)
            self.count = r.json()['count']
        elif r.status_code == 404:
            exit(f'{item}. not found. exiting...')
        else:
            exit('connection error, exiting')


    def find_by_id(self,item, pokeid):
        """
        find pokemon by id
        """
        r = requests.get(
            f'{self._URL}/{item}/{pokeid}'
        )
        if r.status_code == 200:
            data = r.json()
            item = SearchItem(data)
            self.result = item.toString()
        elif r.status_code == 404:
            exit(f'{item} with id {pokeid} not found. Exiting...')
        else:
            exit('connection error occured, exiting. ')

    def find_by_name(self, item, name):
        """
        find pokemon by name
        """
        r = requests.get(
            f'{self._URL}/{item}/{name}'
        )
        if r.status_code == 200:
            self.result = json.dumps(r.json(), indent=4)
        elif r.status_code == 404:
            exit(f'{item} with name {name} not found, exiting.')
        else:
            exit('connection error!')
if __name__ == '__main__':
    c = Client()
    c.result
