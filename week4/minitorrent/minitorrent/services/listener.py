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


response = socket(
    AF_INET, SOCK_STREAM
)

response.bind(("", 37202))
receiving = True
while receiving:

    data, addr = listener.recvfrom(16)
    location = ":".join(f'{value}' for value in addr)
    print(f"{location} {data.decode('utf8')}")
    response.connect((addr[0], 37021))
    response.sendto(b'recieved!', (addr[0], addr[1]))
    receiving = False
