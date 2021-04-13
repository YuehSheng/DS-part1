import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 9

data = pd.read_csv('data.csv', encoding='big5') 

print(data['出生人數'].tolist(),data['死亡人數'].tolist())

name_list = data['村別數'].tolist()
num1_list = data['出生人數'].tolist()
num2_list = data['死亡人數'].tolist()

plt.bar(range(len(num1_list)), num1_list, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='出生人數', lw=1,tick_label=name_list)
plt.bar(range(len(num2_list)), num2_list, alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='死亡人數', lw=1,tick_label=name_list)
plt.legend(loc="upper left")

plt.title("109年11月份金門縣村里人口數")
plt.axis('equal')
plt.savefig('Population.png') 
plt.show()
