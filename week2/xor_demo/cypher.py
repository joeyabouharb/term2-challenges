"""
Cypher Text Decoding,
using key to return the secret
message
"""


def main():
    """
    entry point for application -
    returns decoded string message from cypher
    """
    key = [
        ord(char)
        for char in 'password1'
    ]
    cypher = [
        27, 14, 4,
        18, 21, 26,
        28, 3, 80
    ]
    stream = bytearray(char_generator(zip(key, cypher)))
    return stream.decode('utf8')


def char_generator(paired_list):
    """
    generator function that yields the decoded ascii code
    from the paired up key character (ascii) and encoded ascii cypher
    """
    for (key, cypher) in paired_list:
        yield key ^ cypher


if __name__ == '__main__':
    print(main())
