from shapely import wkt
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from matplotlib import colormaps
plt.rcParams['font.family'] = 'Microsoft JhengHei'

# 讀取 CSV
df = pd.read_csv("data/2020_president_detail_clean.csv")

# 將 geometry 欄位轉換為 shapely 物件（逐一處理避免 MultiPolygon 錯誤）
geometry = df['geometry'].apply(wkt.loads)

# 建立 GeoDataFrame
gdf = gpd.GeoDataFrame(df.drop(columns='geometry'), geometry=geometry, crs='EPSG:4326')
gdf.set_index('name', inplace=True)
# 顯示前幾列確認成功
gdf['winner_votes'] = gdf.apply(lambda row: row[str(row['winner_number'])], axis=1)
gdf['winner_percentage'] = gdf.apply(lambda row: row[str(row['winner_number'])] / row['total'], axis=1)

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# 指定每個候選人對應的 colormap
cmap_map = {
    1: colormaps['Oranges'],
    2: colormaps['Blues'],
    3: colormaps['Greens'],
}

# 建立顏色欄位
# 計算差距比例
def calc_margin(row):
    win_votes = row[str(row['winner_number'])]
    # 對手號碼：假設只有兩人參選
    opponent_number = 1 if row['winner_number'] == 2 else 2
    oppo_votes = row[str(opponent_number)]
    return (win_votes - oppo_votes) / row['total']

gdf['margin_ratio'] = gdf.apply(calc_margin, axis=1)

# 使用 margin_ratio 統一 Normalize
norm = Normalize(vmin=0, vmax=gdf['margin_ratio'].max())

def calculate_color(row):
    cmap = cmap_map[row['winner_number']]
    return cmap(norm(row['margin_ratio']))

gdf['color'] = gdf.apply(calculate_color, axis=1)

print(gdf.winner_percentage)

fig, ax = plt.subplots(figsize=(8, 10))
gdf.plot(ax=ax, color=gdf['color'], edgecolor='black')
plt.title('2020 總統選舉：勝選候選人+得票深淺熱力圖', fontsize=20)
ax.axis('off')

from matplotlib.patches import Patch

# 候選人對照表（可以根據你的實際人名調整）
candidate_names = {
    1: '宋楚瑜',
    2: '韓國瑜',
    3: '蔡英文'
}

# 對照顏色（用漸層的中間色來代表）
color_samples = {
    1: cmap_map[1](0.6),
    2: cmap_map[2](0.6),
    3: cmap_map[3](0.6),
}

# 建立 legend 的 patch
legend_handles = [
    Patch(facecolor=color_samples[k], edgecolor='black', label=candidate_names[k])
    for k in [1, 2, 3]
]
ax.legend(
    handles=legend_handles,
    title='候選人',
    loc='lower left',
    fontsize=18,           # 調整項目名稱字體大小
    title_fontsize=20      # 調整標題「候選人」的字體大小
)

plt.savefig('image/2020_president_detail_map.png', dpi=300, bbox_inches='tight')
plt.show()


