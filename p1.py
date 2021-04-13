import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 9

data = pd.read_csv('data.csv', encoding='big5') 

people = {'總人口數': data['總人口數']} 

# 將 <2% 歸類到其他
threshold = data[data['總人口數'] > data['總人口數'].sum()/100*2]
rest = data[data['總人口數'] <= data['總人口數'].sum()/100*2]['總人口數'].sum()

rest = pd.DataFrame.from_dict( {"總人口數": [rest],
                               "村別數":['其他']}) 
threshold = threshold.append(rest,ignore_index=True)

plt.pie( threshold['總人口數'] ,
    labels = threshold['村別數'],
    autopct='%1.1f%%'
    ) 

plt.title("110年3月份金門縣村里人口數",
    fontdict = {'fontsize': 12,
    'fontweight' : 'bold',
    'horizontalalignment': 'center'}, x=0.5, y=1)
plt.axis('equal')
plt.savefig('Population.png')


move = data[['遷出人數', '遷入人數']]
move.index = data['村別數']
move.plot(kind='bar', stacked=True)


plt.title("110年3月份金門縣村里遷出入人口數")
plt.savefig('PopulationDiff.png')


gender = data[['出生人數', '死亡人數']]
gender.index = data['村別數']
gender.plot.bar(figsize=(20, 5))

plt.title("110年3月份金門縣村里生死長條圖")
plt.savefig('PopulationBD.png')


gender = data[['男數', '女數']]
gender.index = data['村別數']
gender.plot.bar(subplots=True)

plt.title("110年3月份金門縣村里男女長條圖")
plt.savefig('PopulationGender.png')
