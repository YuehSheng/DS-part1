import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 9

data = pd.read_csv('data.csv', encoding='big5') 

people = {'總人口數': data['總人口數']} 

gender = data[['出生人數','死亡人數']]
gender.index = data['村別數']
gender.plot.bar(figsize = (20,5))

plt.title("109年11月份金門縣村里男女長條圖")
plt.savefig('Birth and death.png')