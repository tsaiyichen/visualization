import pandas as pd

df = pd.read_csv('data/2024_president.csv')

#delete useless column, rows
df.drop('備註', axis=1, inplace=True)
df.dropna(axis=0, inplace=True)
df.columns = ['number', 'candidate', 'gender', 'birth', 'party', 'votes', 'isWin']

#merge candidate
for i in range(0, len(df)):
    if i % 2 == 0:
        df.loc[i, 'candidate'] = df.loc[i]['candidate'] + ", " + df.loc[i+1]['candidate']
    else:
        df.drop(axis = 0, index = i, inplace=True)

#remove useless column
df.drop(['gender', 'birth', 'isWin'], axis=1, inplace=True)

#change the index to the election number
df['number'] = df.number.astype(int)
df.set_index('number', inplace=True)

# calculate the total percentage of votes
df['votes'] = df['votes'].str.replace(',', '', regex=False)
df['votes'] = df['votes'].astype(int)
total_votes = df['votes'].sum()
df['percentage'] = (df['votes'] / total_votes).round(4)

#store the df
df.to_csv('data/2024_president_clean.csv', encoding='utf-8-sig')