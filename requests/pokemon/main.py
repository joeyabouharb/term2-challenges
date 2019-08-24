#!/usr/bin/env python3
"""
CLI for our pokemon app
"""
from client import Client

def main():
    """
    mock endpoint that handles interaction with api
    """
    exit_flag = False
    while exit_flag ==  False:
        command = input('Enter a command:  ')
        if command == "hello":
            print("Hello, World!")
        elif command == "pokemon":
            c = Client()
            total = len(c.pokemon)
            if total:
                print(f'There are {total} pokemon')
            else:
                print('Connection Error. ')
        elif command == "exit":
            exit_flag = True

if __name__ == '__main__':
    main()
