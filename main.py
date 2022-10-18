import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
1
n1 = np.random.randint(1,20,15)

print (n1)

n2 = n1.reshape(3,5)

print(n2)

n2[np.isin(n2, np.max(n2 , axis = 1))] = 0

print(n2)
2.1
data = pd.read_csv("E:/data.csv")
2.2
print(data.head())
print(data.info())
2.3
print(data.isnull().any())
2.3
print(data.fillna(data['Calories'].mean(), inplace = True))
print(data.isnull().any())

2.4
print(data.agg({'Duration' : ['min','max','count','mean'], 'Pulse' : ['min','max','count','mean']}))

2.5
print(data.loc[(data['Calories']>500) & (data['Calories']<1000)])

2.6
print(data.loc[(data['Calories']>500) & (data['Pulse']<100)])

2.7

df_modified = data.drop('Maxpulse', axis = 1)

print(df_modified)

2.8

del data['Maxpulse']
print(data)

2.9
print(df_modified.dtypes)
df_modified['Calories'] = df_modified['Calories'].astype(int)
print(df_modified.dtypes)

2.10


plt.scatter(x = list(data['Duration']), y = list(data['Calories']))
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()

3
Programing_languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0,0,0)
plt.pie(popularity, explode=explode, labels=Programing_languages, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()











