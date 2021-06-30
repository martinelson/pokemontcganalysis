from bs4 import BeautifulSoup
import requests

pokemon_types = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying',
                 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dark', 'Dragon', 'Steel', 'Fairy']


def get_name_list():
    table_num = 1
    pokemon_list = []

    response = requests.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")

    while table_num < 9:
        table_div = soup.find("div", class_="mw-parser-output")
        table = table_div.select(f"table:nth-of-type({table_num + 1}) tbody tr td a")
        for link in table:
            if link.text not in pokemon_types and link.text not in pokemon_list:
                pokemon_list.append(link.text)

        table_num += 1

    return pokemon_list

