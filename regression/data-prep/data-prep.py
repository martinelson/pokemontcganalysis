import pandas as pd

df = pd.read_csv("../../data-collection/pokemon-card-price.csv", thousands=',')

df['Pokemon Name'] = df['Pokemon Name'].fillna('N/A')

# Sorting out unavailable prices
df = df.loc[df['Market Price'] > 0]

# Creating df by Rarity and Card Type
df_v1 = df.drop(["Card Name", "Pokemon Name", "Set Name"], axis=1).reset_index().drop("index", axis=1)

df_v1 = pd.get_dummies(df_v1, columns=['Rarity', 'Card Type'], drop_first=True)

# Creating df by Pokemon Name
df_v2 = df.drop(['Card Name', 'Set Name', 'Pokemon Name'], axis=1).reset_index().drop("index", axis=1)

df_v2.loc[(df_v2['Rarity'].str.contains("Rare")), 'Rare'] = 1

df_v2['Rare'] = df_v2['Rare'].fillna(0)

df_v2 = df_v2.drop(['Rarity'], axis=1).reset_index().drop("index", axis=1)

df_v2 = pd.get_dummies(df_v2, columns=['Card Type'], drop_first=True)

# Exporting
df_v1.to_csv("../rarity-card-type.csv", index=False)

df_v2.to_csv("../rarity-card-type-v2.csv", index=False)
