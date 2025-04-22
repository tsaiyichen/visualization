import pandas as pd

df = pd.read_csv('data/2020_party.csv')

df.columns = ['name', 'votes', 'percentage', 'threshold']
df.drop('threshold', axis=1, inplace=True)
df.set_index('name', inplace=True)

df = df[df['percentage'] > 3]

df['votes'] = df['votes'].str.replace(',', '', regex=False)
df['votes'] = df['votes'].astype(int)

df.loc['其他'] = [df.loc['合計']['votes'] - df.head(len(df)-1)['votes'].sum(), 100 - df.head(len(df)-1)['percentage'].sum()]

df.drop('合計', axis=0, inplace=True)
print(df)
df.to_csv('data/2020_party_clean.csv', encoding='utf-8-sig')