import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
    
def get_poke(pokemon):
    """gets a dictorary for a given pokemon name

    Args:
        pokemon (str): name or dex number of pokemon

    Returns:
        dictonary: information about given pokemon
    """

    pokemon = str(pokemon).strip().lower()
    pokemon_url = POKE_API_URL + pokemon

    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    print(f'Getting information for {pokemon}...', end='')
    resp_msg = requests.get(pokemon_url)

    if resp_msg.ok:
        print('success')
        poke_dict = resp_msg.json()
        return poke_dict
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return