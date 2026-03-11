import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)

from sklearn.preprocessing import MinMaxScaler #distribution age
#from sklearn.preprocessing import StandardScaler #distribution gaussienne
from sklearn.decomposition import PCA

df = pd.read_csv('/Users/mariekrammer/Desktop/DI learning/week_3_ML_AI/day_2/datascience_salaries.csv')
#df.info()
#print(df.duplicated())
df = df.drop_duplicates()

#sns.histplot(df,x='salary')
#plt.show()

scaler = MinMaxScaler()
df_new = df.copy()
df_new['salary']=scaler.fit_transform(df_new[['salary']])

#sns.histplot(df,x='salary')
#plt.show()

print(df_new.head(20))
#print(df.nunique())



#df = df.drop(columns = [''])

#for col in df.columns:
    #print(col, df[col].unique())


df_new = pd.get_dummies(df_new,columns=['job_title','job_type','experience_level','salary_currency'])
print(df_new.head())
df_new = df_new.drop(columns = ['location','Unnamed: 0'])
print(df_new.head())

print(df_new.dtypes)
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df_new)
#print(reduced_data)


agg_data = df.groupby(df['experience_level'])['salary'].agg(['mean','mediam'])
print(agg_data)


