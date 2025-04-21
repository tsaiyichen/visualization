import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
plt.rcParams['font.family'] = 'Microsoft JhengHei'

#set color dictionary
color_dic = {
    '中國國民黨': 'blue',
    '民主進步黨': 'green',
    '親民黨': 'orange',
    '台灣民眾黨': 'aqua',
    '時代力量': 'yellow',
    '台灣基進': 'red',
    '其他': 'gray'
}

#load df
df = pd.read_csv('data/2024_party_clean.csv')
df.set_index('number', inplace=True)
df['color'] = df['party'].map(color_dic)

print(df)