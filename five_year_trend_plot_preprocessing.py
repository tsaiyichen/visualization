import pandas as pd

df_2008 = pd.read_csv('data/2008_president_clean.csv', index_col=0)
df_2012 = pd.read_csv('data/2012_president_clean.csv', index_col=0)
df_2016 = pd.read_csv('data/2016_president_clean.csv', index_col=0)
df_2020 = pd.read_csv('data/2020_president_clean.csv', index_col=0)
df_2024 = pd.read_csv('data/2024_president_clean.csv', index_col=1)
df_2024.drop('number', axis=1, inplace=True)
df_2024 = df_2024[['votes', 'party', 'percentage']]

c = '2008'
for i in [df_2008, df_2012, df_2016, df_2020]:
    i.drop('total', axis=0, inplace=True)
    i['year'] = c
    c = str(int(c) + 4)
df_2024['year'] = '2024'

df = pd.concat([df_2008, df_2012, df_2016, df_2020, df_2024])

print(df_2008)
print(df_2012)
print(df_2016)
print(df_2020)
print(df_2024)

print(df)
df.to_csv('data/trend_plot_clean.csv', encoding='utf-8-sig')
