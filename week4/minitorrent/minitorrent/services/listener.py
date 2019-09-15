#! /usr/bin/env python3
from socket import (
    socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP,
    SOL_SOCKET, SO_BROADCAST, SOCK_STREAM
)
import time
import json
import datetime
from minitorrent.services.broadcast import send_broadcast
def listen_in(addresses):
    listener = socket(
        AF_INET, SOCK_DGRAM, IPPROTO_UDP
    )

    listener.bind(("", 37020))

    listening = True
    while listening:
        data, addr = listener.recvfrom(16)
        ip, port = addr
        location = f'{ip}:{port}'
        print(f"{location} {data.decode('utf8')}")
        addresses[ip] = f'{datetime.datetime.today()}'
        yield addresses


if __name__ == '__main__':
    send_broadcast()
    addresses = {}
    for item in listen_in(addresses):
        with open('addresses.json', 'w') as file:
            json.dump(item, file)

