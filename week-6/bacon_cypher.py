"""
defines classes and methods for cypher cryptography
eg. the Bacon Cypher
"""

from string import ascii_lowercase

class Encoder():
    """
    Handles encoding the text by calculating the shift
    values of each letter for substitution cyphers
    """
    def __init__(self, text, **kwargs):
        self.text = text

    def encode(self):
        """
        get the position of each character of the alphabet
        return the positions as a list
        """
        char_positions = []
        for char in self.text:
            index = ascii_lowercase.find(char)
            if not index < 0:
                char_positions.append(index)
        return char_positions


class Decoder():
    """
    decodes the binary data back into text
    """
    def __init__(self, cyphertext, **kwargs):
        self.cyphertext = cyphertext.split(' ')


    def decode(self, cyphertext=None):
        """
        decodes the given cypher as (list) of bytestrings
        and returns the string in as bytarray object.
        :cypher (list of bytes) -> bytes representing each encrypted letter
        returns bytarray object
        """

        stream = (ord(ascii_lowercase[char]) for char in cyphertext)
        return bytearray(stream) # ascii code converted to a bytarray object, which contains the unencryped data


class BaconCypher(Encoder, Decoder):
    """
    responsible for handling the encoding and decoding
    to and from bacon cypher. eg.
    Hello, World ->
    AABBB AABAA ABABA ABABA ABBAB BABAA ABBAB BAAAA ABABA AAABB
    """


    def __init__(self, keys, text='', cyphertext=''):
        """
        upon initialisation, create the decoder and encoder subclasses
        to help with substitution
        :keys (tuple of characters) -> choose what letters to decrypt the message in
        :text (str) -> unencrypted message
        """
        self.key_1, self.key_2 = keys
        self.text = text
        self.cyphertext = cyphertext
        super().__init__(text=text, cyphertext=cyphertext)

    def encode(self):
        """
        encodes text into bacon cypher, by converting
        the binary representation of a letters position
        in the alphabet, and substitutes the numbers to
        the specified cyphers
        """
        # calls the super/ base class Encoder function to return position of letters
        positions_in_alphabet = super().encode()
        bins = []
        # loop to return list to group each encoded letter as a list
        for position in positions_in_alphabet:
            if ord('a') + position >= ord('j'):
                position -= 1
            if ord('a') + position >= ord('v'):
                position -= 1
            text = [char for char in bin(position)[2:]]
            for _ in range(len(text
            ), 5):
                text.insert(0, '0')
            bins.append(text)
        # list to iterate through each item in the list
        # and replaces numbers with their cyphers
        cyphertext = []
        for item in bins:
            encoded = "".join(
                self.key_1 if char == '0' else self.key_2
                for char in item
            )

            cyphertext.append(encoded)
        self.cyphertext = " ".join(cyphertext)


    def decode(self):
        """
        decodes cyphertext back into text
        by counting the number of key_2 in each letter group
        in the cyphertext and converting it back to its letter form
        """
        # generate our indexes to search our character list by converting
        # our binary strings into a list of integers integers
        indexes = []
        for letter in self.cyphertext.split(' '):
            index = int(''.join(
                '0' if element == self.key_1 else '1'
                for element in letter
            ), base=2)
            # i/j and u/v share the same value in this case
            if ord('a') + index >= ord('j'):
                index += 1
            if ord('a') + index >= ord('v'):
                index += 1
            indexes.append(index)
        self.text = super().decode(indexes).decode('ascii') # decode bytearray to string


cypher = BaconCypher(
    ('a', 'b'),
    text='hello world'
)
cypher.encode()
print(cypher.cyphertext)
