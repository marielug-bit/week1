import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)

from sklearn.preprocessing import MinMaxScaler #distribution age
from sklearn.preprocessing import StandardScaler #distribution gaussienne

df2 = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_2/superstore_dataset2011-2015.csv',encoding="latin1")
print(df2.head())


sns.boxplot(data = df2, x='Sales')
plt.show()
scaler = MinMaxScaler()
df2['Sales']= scaler.fit_transform(df2[['Sales']]) #ne change pas la distribution seulement les valeurs


lower = df2['Sales'].quantile(0.10)
upper = df2['Sales'].quantile(0.90)

df2['Sales'] = df2['Sales'].clip(lower, upper) 
sns.histplot(data = df2, x='Sales')
plt.show()