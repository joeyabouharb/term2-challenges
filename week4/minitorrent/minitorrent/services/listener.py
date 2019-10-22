#! /usr/bin/env python3
"""
module responsible for creating a socket
at localhost that listens for incoming connections
creates a list of available hosts on the local network
"""
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
        # print(f"{location} {data.decode('utf8')}")
        if str(ip) not in list(addresses.keys()):
            addresses[ip] = f'{datetime.datetime.today()}'
            time.sleep(1)
            send_broadcast()
        return addresses


if __name__ == '__main__':
    addresses = {}
    send_broadcast()
    listen_in(addresses)
    with open('addresses.json', 'w') as file:
        json.dump(addresses, file)

