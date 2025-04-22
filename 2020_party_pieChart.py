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
df = pd.read_csv('data/2020_party_clean.csv')
df.set_index('name', inplace=True)
df['color'] = df.index.map(color_dic)

#create fig
fig, ax = plt.subplots(figsize=(8, 6.4))

ax = ax.pie(x = df['percentage'], colors=df['color'], labels=df.index, autopct='%.0f%%')

plt.title('2020年全國不分區立委選舉結果')

plt.xlabel('得票比例（獲得席次門檻：5%）')
plt.text(1.2, 0.85, '席次：\n民主進步黨：13\n中國國民黨：13\n台灣民眾黨：5\n時代力量：3',backgroundcolor = 'white', fontsize=12, color = 'black')
fig.patch.set_facecolor('#E5C2A9')

plt.savefig('image/2020_party_pieChart.png', dpi=300, bbox_inches='tight')
plt.show()