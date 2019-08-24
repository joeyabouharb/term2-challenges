#!/usr/bin/env python3
"""
CLI for our pokemon app
"""
import argparse
from client import Client, MAX_POKEMON


def main(args):
    """
    mock endpoint that handles interaction with api
    """
    c = Client()

    if args.subcommand == 'search':
        if args.id:
            find_pokemon_by_id(c, args.id)
        elif args.name:
            find_pokemon_by_name(c, args.name)
    elif args.subcommand == 'list':
        retrieve_all_pokemon(c, args.limit)


def find_pokemon_by_id(c, id):
    c.find_by_id(id)
    print(c.pokemon)


def find_pokemon_by_name(c, name):
    c.find_by_name(name)
    print(c.pokemon)


def retrieve_all_pokemon(c, limit):
    exit_flag = False
    offset = 0

    while exit_flag ==  False:
        c.get_pokemon(limit, offset)
        print(c.pokemon)
        offset += limit

        if offset > MAX_POKEMON:
            exit_flag = True
        input('Press Enter to Retrieve More: ')



if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        prog='Pokedex',
        usage='Program that retrieves pokemon data, or search a known pokemon by id, or name',
        description='Pokedex App that gives you access to all known pokemon. gotta catch them all!'
    )

    SUBCOMMAND = PARSER.add_subparsers(
        title='Subcommands',
        description='execute a subcommand to retrieve data from the pokedex',
        prog='API Requests', dest='subcommand'
    )
    LIST = SUBCOMMAND.add_parser(name='list')
    LIST.add_argument(
        '--limit', type=int, help='limit search results per request', default=0
    )
    POKEMON = SUBCOMMAND.add_parser(name='search')
    POKEMON.add_argument(
        '--id', help='search pokemon via id', type=int, default=20
    )
    POKEMON.add_argument(
        '--name', help='search pokemon via name', type=str, default=''
    )
    ARGS = PARSER.parse_args()
    input(f'{ARGS}')
    main(ARGS)

