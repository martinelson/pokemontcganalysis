import pandas as pd

df = pd.read_csv("../data-collection/pokemon-card-price.csv", thousands=',')

# Sorting out unavailable prices
df = df.loc[df['Market Price'] > 0]


# What are the highest priced cards

def highest_price(df):
    df_result = df.sort_values(by=['Market Price'], ascending=False)[:10]
    return df_result


# Which Set has the highest average value

def highest_avg_sets(df):
    df_mean_set = df.groupby(['Set Name'], as_index=False).mean().sort_values(by=['Market Price'], ascending=False)[:10]
    return df_mean_set


# What is the average price per card rarity type

def highest_avg_rarity(df):
    df_mean_rarity = df.groupby(['Rarity'], as_index=False) \
        .mean().sort_values(by=['Market Price'], ascending=False)
    return df_mean_rarity


# Analysis for total set

df_cards = highest_price(df)[:10]
df_sets = highest_avg_sets(df)[:10]
df_rarity = highest_avg_rarity(df)[:10]
df_cards.to_csv('../analysis/total/total_highest_card_price.csv', index=False)
df_sets.to_csv('../analysis/total/total_highest_avg_set_price.csv', index=False)
df_rarity.to_csv('../analysis/total/total_highest_avg_rarity_price.csv', index=False)

df_by_type = df.groupby(['Card Type'], as_index=False).mean().sort_values(by=['Market Price'], ascending=False)[:10]
df_by_type.to_csv('../analysis/total/total_card_type_avg_price.csv', index=False)

# Filtering for subsections

card_types = ['Energy', 'Supporter', 'Item', 'Stadium', 'Tool', 'Pokemon']

for i in range(len(card_types)):
    df_type = df.loc[df['Card Type'] == card_types[i]].reset_index().drop('index', axis=1)
    df_cards = highest_price(df_type).drop(['Pokemon Name'], axis=1)
    df_sets = highest_avg_sets(df_type)
    df_rarity = highest_avg_rarity(df_type)
    df_cards.to_csv(f'../analysis/{card_types[i].lower()}/{card_types[i].lower()}_highest_card_price.csv', index=False)
    df_sets.to_csv(f'../analysis/{card_types[i].lower()}/'
                   f'{card_types[i].lower()}_highest_avg_set_price.csv', index=False)
    df_rarity.to_csv(f'../analysis/{card_types[i].lower()}/'
                     f'{card_types[i].lower()}_highest_avg_rarity_price.csv', index=False)

# POKEMON SPECIFIC SECTION

df_pokemon = df.loc[(df['Pokemon Name'] != 'nan') & (df['Pokemon Name'] != 'Not found')].reset_index()\
    .drop('index', axis=1)

# Which Pokemon has the highest average value of card

df_sum_pokemon = df_pokemon.groupby(['Pokemon Name'], as_index=False) \
    .mean().sort_values(by=['Market Price'], ascending=False)[:10]

df_sum_pokemon.to_csv('../analysis/pokemon/avg_price_per_pokemon', index=False)

# Count of each pokemon.

df_pokemon = df_pokemon.groupby(['Pokemon Name'], as_index=False)['Market Price'].count() \
    .rename(columns={"Market Price": "count"}).sort_values(by=['count'], ascending=False)[:10]

df_pokemon.to_csv('../analysis/pokemon/count_by_pokemon', index=False)

# Creating POP Series 5 set

df_pop = df.loc[df['Set Name'] == "POP Series 5"].reset_index().drop('index', axis=1)

df_pop.to_csv('../analysis/pokemon/pop_series.csv', index=False)

