

import requests
import requests_cache
import json


class PokemonCache():
    def __init__(self):
        self.request_history = {}

    def retrieve_if_available(self, request):
        """
        retrieves data from request if availailable
        """
        return self.request_history.get(request, None)
    
    def save_to(self, request, payload):
        self.request_history[request] = payload


class Client():
    """
    client service to interact with the api
    """
    _URL = "https://pokeapi.co/api/v2"

    def __init__(self, cache):
        # requests_cache.install_cache(
        #     cache_name='requests', backend='sqlite', expire_after=10000
        # )
        self.result = ''
        self.cache = cache
        self.count = 0

    def get_all(self, item, limit=20, offset=0):
        """
        return all items
        """
        req = f'{self._URL}/{item}?limit={limit}&offset={offset}'
        cached = self.cache.retrieve_if_available(req)
        if cached is not None:
            self.result = cached
        else:
            r = requests.get(req)
            if r.status_code == 200:
                self.result = r.json()
                self.count = r.json()['count']
                self.cache.save_to(req, self.result)
            else:
                self.result = r.status_code
        print(self.result)


    def find_by_id(self,item, pokeid):
        """
        find item by id
        """
        req = f'{self._URL}/{item}/{pokeid}'
        cached = self.cache.retrieve_if_available(req)
        if cached is not None:
            self.result = cached
        else:
            r = requests.get(req)
            if r.status_code == 200:
                self.result = r.json()
                self.cache.save_to(req, self.result)
            else:
                self.result = r.status_code



    def find_by_name(self, item, name):
        """
        find item by name
        """
        req = f'{self._URL}/{item}/{name}'
        cached = self.cache.retrieve_if_available(req)
        if cached is not None:
            self.result = cached
        else:
            r = requests.get(req)
            if r.status_code == 200:
                self.result = r.json()
                self.cache.save_to(req, self.result)
            else:
                self.result = r.status_code


if __name__ == '__main__':
    c = Client()
    c.result
