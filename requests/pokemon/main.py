#!/usr/bin/env python3
"""
CLI for our pokemon app
"""
import argparse
from client import Client


def main(args):
    """
    mock endpoint that handles interaction with api
    """
    c = Client()

    if args.subcommand == 'search':
        if args.id:
            data = find_pokemon_by_id(c, args.id, args.item)
        elif args.name:
            data = find_pokemon_by_name(c, args.name, args.item)
        else:
            exit('no search paramaters were entered! exiting...')
    elif args.subcommand == 'list':
        data = retrieve_all_pokemon(
            c, args.limit, args.offset, args.item
        )
    return data


def find_pokemon_by_id(c, id, item):
    """
    find pokemon by id
    """
    c.find_by_id(item, id)
    return c.result


def find_pokemon_by_name(c, name, item):
    """
    find pokemon by name
    """
    c.find_by_name(item, name)
    return c.result


def retrieve_all_pokemon(c, item, limit=0, offset=0):
    """
    retrieve all pokemon
"""
    c.get_all(item, limit, offset)
    result = c.result
    return result


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        prog='Pokedex',
        usage=(
            'Program that retrieves '
            'pokemon data, or search a known pokemon by id, or name'
        ),
        description=(
            'Pokedex App that gives you access '
            'to all known pokemon. gotta catch them all!'
        )
    )
    SUBCOMMAND = PARSER.add_subparsers(
        title='Subcommands',
        description='retrieve data from the pokedex',
        prog='request data from the API to',
        dest='subcommand',
        required=True
    )
    LIST = SUBCOMMAND.add_parser(
        name='list'
    )
    LIST.add_argument('item', help='item type to list in the pokedex')
    LIST.add_argument(
        '--limit',
        type=int,
        help='limit search results per request',
        default=964
    )
    LIST.add_argument(
        '--offset',
        type=int,
        help='starting point for item listing',
        default=0
    )
    SEARCH = SUBCOMMAND.add_parser(name='search')
    SEARCH.add_argument(
        'item', help='item to search in the pokedex'
    )
    SEARCH.add_argument(
        '--id', help='search pokemon via id',
        type=int, default=0
    )
    SEARCH.add_argument(
        '--name', help='search pokemon via name',
        type=str, default='',
    )
    ARGS = PARSER.parse_args()
    print(ARGS)
    main(ARGS)

