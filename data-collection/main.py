from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from names import get_name_list
from scraping import get_card_data

df_total = pd.DataFrame()
pokemon_names = get_name_list()

chromedriver_path = "/Users/marti/Desktop/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)

pokemon_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Pokemon"
pokemon_pages = 200
energy_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Energy"
energy_pages = 30
supporter_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Supporter"
supporter_pages = 26
item_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Item"
item_pages = 26
stadium_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Stadium"
stadium_pages = 9
tool_url = "https://www.tcgplayer.com/search/pokemon/product?productLineName=pokemon&page=1&ProductTypeName=Cards&CardType=Tool"
tool_pages = 7

urls = [energy_url, supporter_url, item_url, stadium_url, tool_url, pokemon_url]
pages = [energy_pages, supporter_pages, item_pages, stadium_pages, tool_pages, pokemon_pages]
card_types = ['Energy', 'Supporter', 'Item', 'Stadium', 'Tool', 'Pokemon']


for i in range(len(urls)):
    pokemon = []
    rarities, names, prices, sets, types = get_card_data(driver, urls[i], pages[i], card_types[i])
    if card_types[i] == 'Pokemon':
        for card in names:
            v = [pokemon for pokemon in pokemon_names if pokemon in card]
            if len(v) > 0:
                pokemon.append(v[0])
            else:
                pokemon.append("Not found")
    else:
        for card in names:
            pokemon.append("N/A")
    data = {'Card Name': names, 'Rarity': rarities, 'Set Name': sets, 'Card Type': types, 'Pokemon Name': pokemon,
            'Market Price': prices}
    df = pd.DataFrame(data=data)
    df_total = df_total.append(df)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

driver.quit()
print(df_total.head())
print(len(df_total))
df_total.to_csv('pokemon-card-price.csv', index=False, header=True)

