import pandas as pd

df = pd.read_csv('data/2024_party.csv')

df.columns = ['name', 'votes', 'percentage', 'threshold']
df.drop('threshold', axis=1, inplace=True)
df.drop(len(df) - 1, axis=0, inplace=True)
df.set_index('name', inplace=True)
df = df[df['percentage'] > 3]

df.loc['其他'] = 100 - df['percentage'].sum()

df.to_csv('data/2024_party_clean.csv', encoding='utf-8-sig')