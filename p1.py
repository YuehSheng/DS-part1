import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 9

data = pd.read_csv('data.csv', encoding='big5') 

data = data.sort_values(by='總人口數')
people = {'總人口數': data['總人口數']} 

print(data['總人口數'].sum())
threshold = data[data['總人口數'] > data['總人口數'].sum()/100*2]
rest = data[data['總人口數'] <= data['總人口數'].sum()/100*2]['總人口數'].sum()

rest = pd.DataFrame.from_dict( {"總人口數": [rest],
                               "村別數":['其他']}) 
threshold = threshold.append(rest,ignore_index=True)

plt.pie( threshold['總人口數'] ,
    labels = threshold['村別數'],
    autopct='%1.1f%%'
    ) 

plt.title("109年11月份金門縣村里人口數",
    fontdict = {'fontsize': 12,
    'fontweight' : 'bold',
    'horizontalalignment': 'center'}, x=0.5, y=1)
plt.axis('equal')
plt.savefig('Population.png') 
plt.show()

