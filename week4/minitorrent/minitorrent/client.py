"""
client-side application that makes requests for files
to peers in the networl
"""

import requests
from minitorrent.services.spawn import (
    kill, listener
)
listener = listener()


def known_addresses():
    pass

def generator():
    with requests.get('http://0.0.0.0:1234/hello', stream=True) as r:
        r.raise_for_status()
        for chunk in r.iter_content():
            if chunk:
                yield chunk

message = b""
for data in generator():
    message += data
    print(f'\033[1A\033[K{message.decode("utf8")}')

kill(listener)