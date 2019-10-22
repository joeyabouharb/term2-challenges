"""
generators that handle passing data streams to Response
"""


def species_list(client, page):
    """
    generator to handle url data for pokemon species
    """
    start = 15 * (page - 1)
    end = 15 * (page)
    # img_url = "https://raw.githubusercontent.com/"\
    #     "PokeAPI/sprites/master/sprites/pokemon/"
    search_list = client.result['pokemon_species'][start:end]

        
    for species in search_list:
        name, url = species.values()
        id_ = url.split('/').pop(-2)
        # new_url = img_url + id_ + ".png"
        client.find_by_id('pokemon', id_)
        url = \
            client.result['sprites']['front_default']\
            if client.result['sprites']['front_default'] is not None\
            else 'https://via.placeholder.com/150'\

        yield (name, url)

    
def all_pokemon_colors(result):
    """
    generator to yield all pokemon colors
    """
    for item in result['results']:
        color, _ = item.values()
        yield color
