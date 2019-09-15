#! /usr/bin/env python3
from socket import (
    socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP,
    SOL_SOCKET, SO_BROADCAST, SOCK_STREAM
)
import time


def send_broadcast():
    # sets up the socket for IPv4 udp datagram 
    broadcaster = socket(
        AF_INET, SOCK_DGRAM, IPPROTO_UDP
    )
    # set socket options to broadcast globally
    broadcaster.setsockopt(
        SOL_SOCKET, SO_BROADCAST, 1
    )

    # bind socket to broadcast at localhost, port 44444
    broadcaster.bind(("", 44444))
    output = b"is broadcasting!"
    broadcasting = True
    while broadcasting:
        # broadcast to clients listening on port 37020
        broadcaster.sendto(output, ('<broadcast>', 37020))
        print("sending IP!")
        break

if __name__ == '__main__':
    send_broadcast()
    