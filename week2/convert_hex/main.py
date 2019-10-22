#! /usr/bin/env python3
"""
Joseph Abouharb
decodes a secret message from hex value to text string
MIT
"""
from codecs import decode

x = 5

def main(hex_data):
    print(
        decode(hex_data, "hex").decode('utf-8')
    )


if __name__ == '__main__':
    main(
        "49276d20616c7265616479205472616365"
    )
    print(x)

def test():
    def fdfsdfsd():
        pass