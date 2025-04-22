import pandas as pd

df = pd.read_csv('data/2008_president.csv', index_col=0)

df.dropna(axis=0, inplace=True)
df = df.T
df.columns = ['votes', 'party']
df['votes'] = df['votes'].str.replace(',', '', regex=False)
df['votes'] = df['votes'].astype(int)
df['percentage'] = (df['votes'] / df.loc['total']['votes']).round(4)
print(df)
df.to_csv('data/2008_president_clean.csv', encoding='utf-8-sig')