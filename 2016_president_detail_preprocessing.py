import pandas as pd
import geopandas as gpd
region_dictionary = {
    '臺北市': "Taipei City",
    '新北市': "New Taipei City",
    '基隆市': "Keelung City",
    '桃園市': 'Taoyuan',
    '新竹縣': 'Hsinchu',
    '新竹市': 'Hsinchu City',
    '苗栗縣': 'Miaoli',
    '臺中市': 'Taichung City',
    '彰化縣': "Changhua",
    '南投縣': 'Nantou',
    '雲林縣': 'Yunlin',
    '嘉義縣': 'Chiayi',
    '嘉義市': 'Chiayi City',
    '臺南市': 'Tainan City',
    '高雄市': 'Kaohsiung City',
    '屏東縣': 'Pingtung',
    '宜蘭縣': 'Yilan',
    '花蓮縣': 'Hualien',
    '臺東縣': 'Taitung',
    '澎湖縣': 'Penghu',
    '金門縣': 'Kinmen',
    '連江縣': 'Matsu Islands'
}
candidates_dictionary = {
    1: ('朱立倫、王如玄', '中國國民黨'),
    2: ('蔡英文、陳建仁', '民主進步黨'),
    3: ('宋楚瑜、徐欣瑩', '親民黨')
}
df = pd.read_csv('data/2016_president_detail.csv')
df.dropna(axis=0, inplace=True)
df.set_index('行政區別', inplace=True)
df.index = df.index.str.strip()

df.columns = [1, 2, 3, 'total']
df = df.replace(',', '', regex=True)
df = df.astype(int)
df['name'] = df.index.map(region_dictionary)
print(df)
gdf = gpd.read_file('data/tw.json')
df = gdf.merge(df, on='name')
df.set_index('name', inplace=True)

df['winner_number'] = df[[1, 2, 3]].idxmax(axis=1)

print(df)
df.to_csv('data/2016_president_detail_clean.csv', encoding='utf-8-sig')