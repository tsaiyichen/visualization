import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
plt.rcParams['font.family'] = 'Microsoft JhengHei'

#set color dictionary
color_dic = {
    '中國國民黨推薦': 'blue',
    '民主進步黨推薦': 'green',
    '親民黨推薦': 'orange',
    '台灣民眾黨推薦': 'aqua',
    '無黨籍': 'gray'
}

#load df
df = pd.read_csv('data/2024_president_clean.csv')
df.set_index('number', inplace=True)
df['color'] = df['party'].map(color_dic)

#create a figure
fig, ax = plt.subplots(figsize=(12, 6))

#setting the bar chart and its label
bar = ax.bar(x=df['candidate'], height=df['votes'], color=df['color'], width=0.5)
ax.bar_label(container= bar, labels=df['votes'], padding=0, color='black', label_type='center')
df['percentage'] = ((df['percentage']*100).round(2)).astype(str) + '%'
ax.bar_label(container= bar, labels=df['percentage'], padding=-2, color='black', label_type='edge')

#setting the title, xlabel, ylabel
plt.title('2024年總統副總統選舉結果')
plt.xlabel('候選人')
plt.ylabel('得票數（單位：萬）')
def to_ten_thousand(x, pos):
    return f'{x / 10000:.0f}'
formatter = ticker.FuncFormatter(to_ten_thousand)
ax.yaxis.set_major_formatter(formatter) #y-axis scale

#setting the color of the background
fig.patch.set_facecolor('#E5C2A9')
ax.patch.set_facecolor('#E5C2A9')

plt.savefig('image/2024_president_barChart.png', dpi=300, bbox_inches='tight')
plt.show()
