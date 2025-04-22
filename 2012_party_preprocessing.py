import pandas as pd

df = pd.read_csv('data/2012_party.csv')

df.columns = ['name', 'votes', 'percentage']
df.set_index('name', inplace=True)
df.loc['合計'] = [df['votes'].sum(), 100]
df = df[df['percentage'] > 3]

df.loc['其他'] = [df.loc['合計']['votes'] - df.head(len(df)-1)['votes'].sum(), 100 - df.head(len(df)-1)['percentage'].sum()]

df.drop('合計', axis=0, inplace=True)
print(df)
df.to_csv('data/2012_party_clean.csv', encoding='utf-8-sig')