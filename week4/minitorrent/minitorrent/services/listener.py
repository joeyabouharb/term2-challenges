#! /usr/bin/env python3
from socket import (
    socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP,
    SOL_SOCKET, SO_BROADCAST, SOCK_STREAM
)

listener = socket(
    AF_INET, SOCK_DGRAM, IPPROTO_UDP
)
listener.setsockopt(
    SOL_SOCKET, SO_BROADCAST, 1
)
listener.bind(("", 37020))

respond = socket(
    AF_INET, SOCK_STREAM
)

listening = True
while listening:
    data, addr = listener.recvfrom(16)
    location = ":".join(f'{value}' for value in addr)
    print(f"{location} {data.decode('utf8')}")
    
    listening = False
