import datetime
import requests
dt_s = '2019-10-08'
form = '%Y-%m-%d'
date = datetime.datetime.strptime(dt_s, form)
print(date)

class Client:
    def __init__(self):
        self.URL = 'https://financialmodelingprep.com/api/v3/'
        self.route = 'historical-price-full/'
        self.args = 'AAPL?serietype=line'
        self.result = ''
    def get_request(self):
        """
        get request data
        """
        r = requests.get(
            f'{self.url}'
            f'{self.route}'
            f'{self.args}')
        
        if r.status_code == 200:
            self.res