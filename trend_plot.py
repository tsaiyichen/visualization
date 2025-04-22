import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.rcParams['font.family'] = 'Microsoft JhengHei'

# 讀取資料
df = pd.read_csv("data/trend_plot_clean.csv")

# 政黨顏色字典
color_dic = {
    '中國國民黨推薦': 'blue',
    '民主進步黨推薦': 'green',
    '親民黨推薦': 'orange',
    '台灣民眾黨推薦': 'aqua',
    '無黨籍': 'gray'
}
df['percentage'] = (df['percentage'] * 100).round(2)
# 建立雙 Y 軸圖表
fig, ax1 = plt.subplots(figsize=(10,8))
ax2 = ax1.twinx()

# 把資料年份和政黨整理出來
years = sorted(df['year'].unique())
parties = df['party'].unique()

bar_width = 0.5
offsets = {party: i * bar_width - (len(parties) - 1) * bar_width / 2 for i, party in enumerate(parties)}

for party in parties:
    sub = df[df['party'] == party]

    # 畫透明長條圖
    ax1.bar(
        [y + offsets[party] for y in sub['year']],
        sub['votes'],
        width=bar_width,
        label=party,
        color=color_dic.get(party, 'black'),
        alpha=0.6  # ✅ 設定透明度
    )

    # 折線圖（只畫藍綠）
    if party in ['中國國民黨推薦', '民主進步黨推薦']:
        ax2.plot(
            sub['year'],
            sub['percentage'],
            label=f"{party} 得票率",
            linestyle='--',
            marker='o',
            color=color_dic.get(party, 'black')
        )

# 標籤與圖例
ax1.set_xlabel("選舉年份")
ax1.set_ylabel("得票數（萬）")
ax2.set_ylabel("得票率（%）")
plt.title("歷屆總統大選 各政黨得票數與主要政黨得票率")
ax1.set_xticks(years)
ax1.set_xticklabels([str(y) for y in years])
def to_ten_thousand(x, pos):
    return f'{x / 10000:.0f}'
formatter = ticker.FuncFormatter(to_ten_thousand)
ax1.yaxis.set_major_formatter(formatter)
ax2.set_ylim(0, 100)
# 合併兩個圖例
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

plt.tight_layout()
plt.savefig('image/president_trend.png', dpi=300, bbox_inches='tight')
plt.show()
